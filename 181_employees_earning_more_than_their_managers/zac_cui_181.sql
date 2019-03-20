--	Author: Zac Cui
--	Created Date: 2019-03-13 13:23:47

SELECT 
    e.Name AS 'Employee'
FROM
    Employee e, Employee m
WHERE
    m.id = e.ManagerId
AND
    m.Salary < e.Salary
