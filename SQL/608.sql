SELECT ID,
    CASE WHEN p_id IS NULL THEN 'Root'
    WHEN id IN (SELECT p_id FROM tree) THEN 'Inner'
    else 'Leaf' END AS 'Type'
FROM Tree