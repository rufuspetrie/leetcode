SELECT employee_id
FROM Employees
WHERE employee_id NOT IN (SELECT employee_id FROM salaries)
UNION Select employee_id
FROM Salaries
WHERE employee_id NOT IN (SELECT employee_id FROM employees)
ORDER BY employee_id