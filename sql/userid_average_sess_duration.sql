SELECT "userId", AVG("duration") AS average_session_duration
FROM sessions
GROUP BY "userId"
HAVING AVG("duration") > 1
