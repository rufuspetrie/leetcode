SELECT user_id as buyer_id, join_date, COUNT(DISTINCT Orders.order_id) AS orders_in_2019
FROM Users
LEFT JOIN Orders
ON Orders.buyer_id = Users.user_id
AND year(Orders.order_date) = '2019'
GROUP BY Users.user_id