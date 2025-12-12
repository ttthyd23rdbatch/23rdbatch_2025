CREATE TABLE employees (
    id SERIAL PRIMARY KEY,
    name TEXT,
    salary INT
);

INSERT INTO employees (name, salary)
VALUES ('manohar', 60000);

SELECT * FROM employees;
