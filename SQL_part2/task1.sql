--#1
SELECT em.first_name, em.last_name, em.department_id, dep.department_name
FROM employees 'em'
INNER JOIN department 'dep'
ON em.department_id = dep.department_id;
--#2
SELECT em.first_name, em.last_name, dep.department_name, loc.city, loc.state_province
FROM employees 'em'
INNER JOIN department 'dep', locations 'loc'
ON em.department_id = dep.department_id
AND dep.location_id = loc.location_id;
--#3
SELECT em.first_name, em.last_name, em.department_id, dep.department_name
FROM employees 'em'
INNER JOIN department 'dep'
ON em.department_id = dep.department_id
AND (em.department_id = 80 OR em.department_id = 40);
--#4
SELECT department_name
FROM department
WHERE department_id NOT IN (SELECT department_id FROM employees);
--#5
SELECT em.first_name, (
SELECT first_name
FROM employees
WHERE employee_id = dep.manager_id) 'manager first name'
FROM employees 'em'
INNER JOIN departments 'dep' ON dep.department_id = em.department_id;
--#6
SELECT j.job_title 'Job Title', em.first_name ||' '|| em.last_name 'Full Name', j.max_salary-em.salary 'Difference'
FROM employees 'em'
INNER JOIN jobs 'j' ON em.job_id = j.job_id;
--#7
SELECT j.job_title, AVG(em.salary)
FROM employees 'em'
INNER JOIN jobs 'j' ON j.job_id = em.job_id
GROUP BY j.job_title;
--#8
SELECT em.first_name || ' ' || em.last_name 'Full Name', em.salary 'Salary'
FROM employees 'em'
INNER JOIN departments 'dep' ON dep.department_id = em.department_id
INNER JOIN locations 'loc' ON loc.location_id = dep.location_id
WHERE loc.city = 'London';
--#9
SELECT dep.department_name, COUNT(em.department_id)
FROM department 'dep'
INNER JOIN employees 'em' ON dep.department_id = em.department_id
GROUP BY dep.department_name;
