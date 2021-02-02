SELECT em.first_name, em.last_name, em.department_id, dep.department_name
FROM employees as 'em', department as 'dep'
WHERE em.department_id = dep.department_id;

SELECT em.first_name, em.last_name, dep.department_name, loc.city, loc.state_province
FROM employees as 'em', department as 'dep', locations as 'loc'
WHERE em.department_id = dep.department_id
AND dep.location_id = loc.location_id;

SELECT em.first_name, em.last_name, em.department_id, dep.department_name
FROM employees as 'em', department as 'dep'
WHERE em.department_id = dep.department_id AND (em.department_id = 80 OR em.department_id = 40);

SELECT department_name
FROM department
WHERE department_id NOT IN (SELECT department_id FROM employees);

SELECT em.first_name
FROM employees as 'em', department as 'dep'
WHERE em.department_id = dep.department_id;
