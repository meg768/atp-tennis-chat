SELECT p.id,p.name,p.highest_rank,
SUM(CASE WHEN x.opponent_rank BETWEEN 1 AND 10 AND x.won=1 THEN 1 ELSE 0 END) wins,
SUM(CASE WHEN x.opponent_rank BETWEEN 1 AND 10 AND x.won=0 THEN 1 ELSE 0 END) losses,
SUM(CASE WHEN x.opponent_rank IS NULL OR x.opponent_rank<=0 THEN 1 ELSE 0 END) missing_rank
FROM players p LEFT JOIN (
SELECT winner player,loser_rank opponent_rank,1 won FROM matches WHERE status IN ('Completed','Aborted')
UNION ALL
SELECT loser player,winner_rank opponent_rank,0 won FROM matches WHERE status IN ('Completed','Aborted')
) x ON x.player=p.id
WHERE p.highest_rank=1 OR p.id='Z355'
GROUP BY p.id,p.name,p.highest_rank;
