SELECT name, 
SUM(CASE WHEN Rides.user_id = Users.id THEN distance ELSE 0 END) as travelled_distance
FROM Users
LEFT JOIN Rides
ON Rides.user_id = Users.id
GROUP BY Rides.user_id
ORDER BY travelled_distance DESC, name ASC