SELECT employee_id, CASE when employee_id % 2 = 1 AND name NOT LIKE 'M%' THEN salary ELSE 0 END AS bonus
FROM employees
ORDER BY employee_id