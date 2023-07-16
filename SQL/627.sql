UPDATE Salary
SET sex = CASE
    when sex = 'm' then 'f'
    when sex = 'f' then 'm' END