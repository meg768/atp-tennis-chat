BEGIN
    /*
    WIN_PROBABILITY_TA(playerID, opponentID, surface)

    Purpose
    - Return the fair Tennis Abstract Elo win probability for playerID against
      opponentID.
    - This is the canonical TA model. It performs no pricing and applies no
      margin; PLAYER_ODDS converts the probability to decimal odds.

    Input
    - playerID, opponentID:
      ATP player id or free-text player name resolved through PLAYER_LOOKUP.
    - surface:
      Hard, Clay, or Grass (case-insensitive). NULL, empty, or another value
      selects overall Tennis Abstract Elo.

    Output
    - Fair probability for playerID between 0 and 1.
    - NULL when either player cannot be resolved, both inputs resolve to the
      same player, or the selected stored Elo is missing or non-positive.

    Model
    - Select overall or surface-specific Tennis Abstract Elo from players.
    - Apply the standard Elo expectation formula:
      1 / (1 + 10 ^ ((opponentElo - playerElo) / 400)).
    */

    DECLARE v_player_id VARCHAR(32) DEFAULT NULL;
    DECLARE v_opponent_id VARCHAR(32) DEFAULT NULL;
    DECLARE v_surface VARCHAR(50) DEFAULT NULL;
    DECLARE v_elo_player DOUBLE DEFAULT NULL;
    DECLARE v_elo_opponent DOUBLE DEFAULT NULL;

    IF playerID IS NULL OR TRIM(playerID) = '' OR opponentID IS NULL OR TRIM(opponentID) = '' THEN
        RETURN NULL;
    END IF;

    SET v_player_id = PLAYER_LOOKUP(playerID);
    SET v_opponent_id = PLAYER_LOOKUP(opponentID);
    IF v_player_id IS NULL OR v_opponent_id IS NULL OR UPPER(v_player_id) = UPPER(v_opponent_id) THEN
        RETURN NULL;
    END IF;

    SET v_surface = UPPER(NULLIF(TRIM(surface), ''));

    SELECT CASE v_surface
        WHEN 'HARD' THEN elo_rank_hard
        WHEN 'CLAY' THEN elo_rank_clay
        WHEN 'GRASS' THEN elo_rank_grass
        ELSE elo_rank
    END
    INTO v_elo_player
    FROM players WHERE id = v_player_id LIMIT 1;

    SELECT CASE v_surface
        WHEN 'HARD' THEN elo_rank_hard
        WHEN 'CLAY' THEN elo_rank_clay
        WHEN 'GRASS' THEN elo_rank_grass
        ELSE elo_rank
    END
    INTO v_elo_opponent
    FROM players WHERE id = v_opponent_id LIMIT 1;

    IF v_elo_player IS NULL OR v_elo_opponent IS NULL OR v_elo_player <= 0 OR v_elo_opponent <= 0 THEN
        RETURN NULL;
    END IF;

    RETURN 1 / (1 + POW(10, (v_elo_opponent - v_elo_player) / 400));
END