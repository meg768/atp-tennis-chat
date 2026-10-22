WITH obs AS (
SELECT m.id,m.winner player,1 won,m.loser opponent,m.loser_rank opponent_rank,e.date,e.name,e.surface,m.round,m.score,m.status FROM matches m JOIN events e ON e.id=m.event WHERE m.winner IN (%s,%s,%s,%s,%s,%s,%s) AND e.date BETWEEN '2025-10-21' AND '2026-10-21' AND m.status IN ('Completed','Aborted')
UNION ALL
SELECT m.id,m.loser player,0 won,m.winner opponent,m.winner_rank opponent_rank,e.date,e.name,e.surface,m.round,m.score,m.status FROM matches m JOIN events e ON e.id=m.event WHERE m.loser IN (%s,%s,%s,%s,%s,%s,%s) AND e.date BETWEEN '2025-10-21' AND '2026-10-21' AND m.status IN ('Completed','Aborted'))
SELECT obs.*,p.name opponent_name FROM obs LEFT JOIN players p ON p.id=obs.opponent ORDER BY date DESC,id DESC