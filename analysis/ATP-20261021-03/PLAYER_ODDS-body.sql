BEGIN
    /*
    PLAYER_ODDS(playerA, playerB, surface)

    Purpose
    - Return priced decimal odds for two players in the requested matchup.
    - Resolve both inputs through PLAYER_LOOKUP and return both the TA and GPT
      models in one result set.

    Input
    - playerA, playerB:
      ATP player id or free-text player name.
    - surface:
      Hard, Clay, or Grass (case-insensitive). NULL, empty, or another value
      selects each model's surface-neutral behavior.

    Output columns
    - player: resolved players.id.
    - name: resolved player name.
    - TA: Tennis Abstract Elo decimal odds rounded to two decimals.
    - GPT: weighted GPT-model decimal odds rounded to two decimals.
    - Two rows in input order: playerA first, playerB second.

    Pricing
    - Fair probabilities come from WIN_PROBABILITY_TA and WIN_PROBABILITY_GPT.
    - The opponent probability is 1 minus the player probability.
    - Every probability is multiplied by 1.05 and clamped to 0.001..0.999
      before conversion with 1 / p. Each model therefore has a 5 percent
      pricing margin and never returns decimal odds below 1.00.

    Validation and empty results
    - Returns an empty result set when either player cannot be resolved, both
      inputs resolve to the same player, or either model returns an invalid
      probability.

    Example usage
    - CALL PLAYER_ODDS('S0AG', 'A0E2', 'Hard');
    - CALL PLAYER_ODDS('Sinner', 'Alcaraz', NULL);
    */


    DECLARE resolvedPlayerA VARCHAR(32) DEFAULT NULL;
    DECLARE resolvedPlayerB VARCHAR(32) DEFAULT NULL;
    DECLARE normalizedSurface VARCHAR(50) DEFAULT NULL;
    DECLARE taProbabilityA DOUBLE DEFAULT NULL;
    DECLARE taProbabilityB DOUBLE DEFAULT NULL;
    DECLARE gptProbabilityA DOUBLE DEFAULT NULL;
    DECLARE gptProbabilityB DOUBLE DEFAULT NULL;

    SET resolvedPlayerA = PLAYER_LOOKUP(playerA);
    SET resolvedPlayerB = PLAYER_LOOKUP(playerB);
    SET normalizedSurface = NULLIF(TRIM(surface), '');

    IF resolvedPlayerA IS NULL
        OR resolvedPlayerB IS NULL
        OR UPPER(resolvedPlayerA) = UPPER(resolvedPlayerB)
    THEN
        SELECT
            id AS player,
            name AS name,
            CAST(NULL AS DECIMAL(10,2)) AS TA,
            CAST(NULL AS DECIMAL(10,2)) AS GPT
        FROM players
        WHERE 1 = 0;
    ELSE
        SET taProbabilityA = WIN_PROBABILITY_TA(resolvedPlayerA, resolvedPlayerB, normalizedSurface);
        SET gptProbabilityA = WIN_PROBABILITY_GPT(resolvedPlayerA, resolvedPlayerB, normalizedSurface);

        IF taProbabilityA IS NULL OR taProbabilityA <= 0 OR taProbabilityA >= 1
            OR gptProbabilityA IS NULL OR gptProbabilityA <= 0 OR gptProbabilityA >= 1
        THEN
            SELECT
                id AS player,
                name AS name,
                CAST(NULL AS DECIMAL(10,2)) AS TA,
                CAST(NULL AS DECIMAL(10,2)) AS GPT
            FROM players
            WHERE 1 = 0;
        ELSE
            SET taProbabilityB = 1 - taProbabilityA;
            SET gptProbabilityB = 1 - gptProbabilityA;

            SELECT
                p.id AS player,
                p.name AS name,
                ROUND(1 / LEAST(0.999, GREATEST(0.001, taProbabilityA * 1.05)), 2) AS TA,
                ROUND(1 / LEAST(0.999, GREATEST(0.001, gptProbabilityA * 1.05)), 2) AS GPT
            FROM players p
            WHERE p.id = resolvedPlayerA

            UNION ALL

            SELECT
                p.id AS player,
                p.name AS name,
                ROUND(1 / LEAST(0.999, GREATEST(0.001, taProbabilityB * 1.05)), 2) AS TA,
                ROUND(1 / LEAST(0.999, GREATEST(0.001, gptProbabilityB * 1.05)), 2) AS GPT
            FROM players p
            WHERE p.id = resolvedPlayerB;
        END IF;
    END IF;
END