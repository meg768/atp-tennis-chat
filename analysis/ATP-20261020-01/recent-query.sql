WITH obs AS (
 SELECT m.id,m.winner AS player_id,1 AS won,m.loser AS opponent_id,m.loser_rank AS opponent_rank,e.date,e.name,e.type,e.surface,m.round,m.score,m.status
 FROM matches m JOIN events e ON e.id=m.event WHERE m.winner IN (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s) AND e.date >= '2025-10-21' AND e.date <= '2026-10-20' AND m.status IN ('Completed','Aborted')
 UNION ALL
 SELECT m.id,m.loser AS player_id,0 AS won,m.winner AS opponent_id,m.winner_rank AS opponent_rank,e.date,e.name,e.type,e.surface,m.round,m.score,m.status
 FROM matches m JOIN events e ON e.id=m.event WHERE m.loser IN (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s) AND e.date >= '2025-10-21' AND e.date <= '2026-10-20' AND m.status IN ('Completed','Aborted')
) SELECT obs.*,p.name AS opponent FROM obs LEFT JOIN players p ON p.id=obs.opponent_id ORDER BY date DESC,id DESC