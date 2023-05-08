DELETE p
FROM Person p, Person q
WHERE p.email = q.email and p.Id > q.Id