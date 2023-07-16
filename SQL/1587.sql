SELECT name, sum(amount) as balance
FROM Transactions
LEFT JOIN Users
ON Transactions.account = Users.account
GROUP BY Transactions.account
HAVING SUM(amount) >= 11000