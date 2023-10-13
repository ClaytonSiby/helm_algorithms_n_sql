SELECT userId, AVG(duration) AS average_session_duration
FROM enrollments
GROUP BY userId
HAVING COUNT(*) > 1
