# Granskning av TA-odds i MariaDB

Direkt avläsning 2026-10-21 kl. 17.53 Europe/Stockholm. Inga databasändringar.

## Beräkningskedja

`WIN_PROBABILITY_TA(A,B,surface)` väljer lagrad Elo från `players`: `elo_rank_hard`, `elo_rank_clay`, `elo_rank_grass`, annars `elo_rank`. Kolumnerna är heltal. För ett giltigt underlag används dess Elo direkt; funktionen blandar inte med total Elo. Om vald Elo saknas eller är <= 0 returneras NULL.

`pA = 1 / (1 + 10^((eloB - eloA)/400))`

Detta är modellens vinstchans utan prispåslag. Underliggande fair odds är `1/pA`. TA-kolumnen i `PLAYER_ODDS` är en lokal prissättning från dessa Elo-värden, inte bookmakerodds hämtade från Tennis Abstract.

`PLAYER_ODDS` sätter `pB = 1-pA` och returnerar för varje sida:

```sql
ROUND(1 / LEAST(0.999, GREATEST(0.001, p * 1.05)), 2)
```

Samma prissättning tillämpas på GPT-modellens sannolikheter. Proceduren returnerar tomt om endera modellen ger en ogiltig sannolikhet.

## Vad fem procent betyder

Utan aktiva gränsvärden eller avrundning är oddset `fair_odds / 1.05`. Oddsminskningen är då 4,7619 %, och summan av de två prissatta implicita sannolikheterna är 105 %: 5 % överrundning. Det är inte fem procentenheter på vardera sidans sannolikhet och inte `fair_odds * 0.95`.

Prissättningen motsvarar i detta idealfall 4,7619 % förväntad förlust per insatsenhet vid modellens sannolikheter. Överrundning är inte samma sak som faktisk bookmakerintäkt.

Efter avrundning kan överrundningen avvika åt båda håll. Vid extrem favorit/outsider kan begränsningen 0,001–0,999 ge större avvikelser redan före avrundning. Exempel med syntetisk 96 % favorit: prissatta sannolikheter 0,999 och 0,042 ger 4,1 % överrundning före avrundning; returnerade odds 1,00 och 23,81 ger cirka 4,20 %.

## Verifierade exempel

| Hard | Elo | Modellchans | Fair odds | TA från PLAYER_ODDS |
|---|---:|---:|---:|---:|
| Jacob Fearnley | 1676 | 58,5499 % | 1,70795 | 1,63 |
| Clement Chidekh | 1616 | 41,4501 % | 2,41254 | 2,30 |
| Jan-Lennard Struff | 1667 | 78,7927 % | 1,26915 | 1,21 |
| Gauthier Onclin | 1439 | 21,2073 % | 4,71535 | 4,49 |

Fearnley/Chidekh: `1/1.63 + 1/2.30 - 1 = 4,82795 %`.
Struff/Onclin: `1/1.21 + 1/4.49 - 1 = 4,91634 %`.
50/50-modell ger oavrundat 1,9047619 per sida, returnerat 1,90 och därmed 5,26316 % överrundning från visade odds.

Egen beräkning från sannolikheterna matchade procedurens TA-priser för fyra kontroller: två Hard-matcher samt Fearnley/Chidekh med NULL och Clay. Omvända TA-anrop summerade till 1 i alla fyra kontroller.

## Praktisk användning

- Vid prisjämförelse med Svenska Spel: använd TA från `PLAYER_ODDS` direkt, benämnt "TA-odds med 5 % sannolikhetspåslag; överrundningen kan avvika efter avrundning och begränsning".
- Vid beräkning av modell-EV: använd `WIN_PROBABILITY_TA` utan påslag i `p * erbjudet_odds - 1`. Använd inte `1/TA_odds` som marginfri vinstchans.
- Fearnleys tidigare angivna 1,63 respektive fair odds 1,71 och modell-EV +8,9 % vid erbjudet 1,86 var matematiskt konsekventa.

Källor: `PLAYER_ODDS-body.sql` och `WIN_PROBABILITY_TA-body.sql` är direkt avlästa rutintexter. Databasens LAST_ALTERED var 2026-07-14 för båda. `audit.json` innehåller Elo, sannolikheter, procedursvar, oavrundade odds och syntetiska gränsfall. `routine-query.sql` dokumenterar hämtningen.
