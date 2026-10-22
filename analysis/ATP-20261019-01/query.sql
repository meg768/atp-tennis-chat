WITH young AS (SELECT id,name,birthdate,`rank` FROM players WHERE birthdate>'2003-10-19' AND birthdate<='2026-10-19' AND `rank` BETWEEN 1 AND 100), obs AS (
SELECT p.id,e.date,m.id mid,m.winner_rank r FROM young p JOIN matches m ON m.winner=p.id JOIN events e ON e.id=m.event WHERE e.date<='2025-10-19' AND m.winner_rank>0
UNION ALL
SELECT p.id,e.date,m.id,m.loser_rank FROM young p JOIN matches m ON m.loser=p.id JOIN events e ON e.id=m.event WHERE e.date<='2025-10-19' AND m.loser_rank>0
), ranked AS (SELECT *,ROW_NUMBER() OVER(PARTITION BY id ORDER BY date DESC,mid DESC) rn FROM obs)
SELECT p.*,r.r old_rank,r.date observed_date,r.r-p.`rank` gain FROM young p LEFT JOIN ranked r ON p.id=r.id AND r.rn=1 ORDER BY gain DESC,p.birthdate DESC