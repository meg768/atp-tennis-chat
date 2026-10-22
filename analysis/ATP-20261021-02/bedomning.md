# Dagens återstående spel, 21 oktober 2026

Screening kl. 14.27 svensk tid. Sex kommande ATP-singelmatcher samma svenska kalenderdag i https://tennis.egelberg.se/api/oddset. Påbörjade matcher exkluderas. Detta är ett subjektivt spelurval efter screening, inte en ranking efter modellgap.

Direkt MariaDB via scripts/database.py: CALL PLAYER_ODDS(A,B,'Hard') och SELECT WIN_PROBABILITY_TA(A,B,'Hard'). Båda anrop använder respektive spelares ATP-ID från flödet. TA- och GPT-priserna från PLAYER_ODDS inkluderar redan standardpåslaget 5 %. Inget ytterligare påslag. GPT och TA ska inte betraktas som oberoende bekräftelser. Rådata: screening.json, slutkontroll: final-odds-check.json.

Förstaval Fearnley mot Chidekh: SS 1,86, TA 1,63, GPT 1,61. TA utan marginal: 58,55 % och fair odds 1,71; modell-EV vid 1,86 cirka +8,9 % (p*odds-1), förutsatt korrekt modellchans. Subjektiv lägsta spelgräns 1,80. Fearnley nådde final i Olbia och slog Gaston 6–3, 6–0 i Bryssel. Chidekh vann Mouilleron och slog van de Zandschulp 6–1, 6–4 efter kvalet i Bryssel. Bådas form ger anledning till en försiktig bedömning.

Struff mot Onclin: SS 1,32, TA 1,21, GPT 1,29. TA utan marginal 78,79 %, modell-EV +4,0 %. För tunn fördel vid nuvarande pris med tanke på modellskillnaden; bevaka först vid 1,40 (subjektiv gräns).

Moutet SS 2,00, TA 1,38, GPT 1,63: avstå trots modellgap på grund av 3 h 21 min mot Humbert dagen före och spelarens egen osäkerhet om handleden. https://www.universtennis.com/2026/10/20/atp-250-lyon-corentin-moutet-apres-sa-victoire-contre-ugo-humbert-jai-mal-depuis-le-debut-de-lannee/

Goffin SS 2,63, TA 1,35, GPT 1,81: avstå. Bara 3–12 i databasens registrerade Completed/Aborted-matcher senaste året, 2025-10-21 till 2026-10-21 baserat på turneringsstartdatum. Förlorade senast registrerat 1–6, 0–6 mot Chidekh. Modellen kan övervärdera äldre spelstyrka.

Kukushkin SS 8,50 visar positiv TA-EV, men den registrerade historiken har ett stort glapp mellan juni och oktober och ger otillräckligt stöd för ett spelval. Tsitsipas och Paul saknar positiv TA-EV till nuvarande priser.

Formunderlag: recent.json; query och parametrar sparade separat. Alla nivåer, inklusive kval och Davis Cup, Completed/Aborted, exklusive walkover. Eventdatum är turneringsstart, inte matchdatum. Ordning inom turnering härleds från omgång. Formresultaten Gaston–Fearnley och Chidekh–van de Zandschulp kontrollerades även mot https://www.tennisactu.net/news-atp-bruxelles-hugo-gaston-coince-d-entree-contre-jacob-fearnley-127725.html och finns nu i databasen.

Elo separerar inte uttryckligen inomhus och utomhus. Modellchans är ingen garanti och inga nya matcher har lagts in manuellt. Tider är preliminära och priser kan ändras.
