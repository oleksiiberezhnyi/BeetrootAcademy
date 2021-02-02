sqlite3 hr.db
SELECT first_name as 'First Name', last_name as 'Last Name' from employees;
SELECT * FROM employees WHERE department_id=50;
SELECT * FROM employees ORDER BY first_name DESC;
SELECT first_name, last_name, salary, salary*0.12 as PF FROM employees;
SELECT MIN(salary) as MIN, MAX(salary) as MAX FROM employees;
SELECT first_name as 'First Name', last_name as 'Last Name', round(salary/12, 2) as 'Monthly Salary' FROM employees;