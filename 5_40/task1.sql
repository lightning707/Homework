/*write a query in SQL to display the first name, last name, department number,
 and department name for each employee*/
 SELECT em.first_name, em.last_name, em.department_id, dp.department_name
 FROM employees em JOIN department dp
 USING(department_id);
 
/*write a query in SQL to display the first and last name, department, city,
 and state province for each employee*/
 SELECT em.first_name, em.last_name, dp.department_name, loc.city, loc.state_province
 FROM employees em JOIN department dp
 USING(department_id)
 JOIN locations loc
 ON dp.location_id = loc.location_id;
 
/*write a query in SQL to display the first name, last name, department number, 
and department name, for all employees for departments 80 or 40*/
SELECT em.first_name, em.last_name, dp.department_id, dp.department_name
FROM employees em JOIN department dp
USING(department_id)
WHERE dp.department_id = 40 or dp.department_id = 80;

/*write a query in SQL to display all departments including those where
 does not have any employee*/
SELECT DISTINCT department_name, dp.*
FROM department dp
LEFT JOIN employees em
USING(department_id);

/*write a query in SQL to display the first name of all employees 
including the first name of their manager*/
SELECT em.first_name, man.first_name as 'Manager name'
FROM employees em JOIN employees man
WHERE em.manager_id = man.employee_id;

/*write a query in SQL to display the job title, full name 
(first and last name ) of the employee, and the difference between 
the maximum salary for the job and the salary of the employee*/
SELECT jobs.job_title, (em.first_name || ' ' || em.last_name) as 'Full name', 
(jobs.max_salary - em.salary) as 'Salary difference'
FROM employees em JOIN jobs
USING(job_id);

/*write a query in SQL to display the job title 
and the average salary of employees*/
SELECT jobs.job_title, (em.first_name || ' ' || em.last_name) as 'Full name',
AVG(em.salary)
FROM employees em JOIN jobs
USING(job_id)
GROUP BY jobs.job_id;

/*write a query in SQL to display the full name (first and last name), 
and salary of those employees who work in any department located in London*/
SELECT (em.first_name || ' ' || em.last_name) as 'Full name', em.salary
FROM employees em JOIN departments dp
USING(department_id)
JOIN locations loc
USING(location_id);

/*write a query in SQL to display the department name and the number
 of employees in each department*/
SELECT dp.department_name, COUNT(em.department_id) as 'Number of employees'
FROM employees em JOIN department dp
USING(department_id)
GROUP BY department_id;