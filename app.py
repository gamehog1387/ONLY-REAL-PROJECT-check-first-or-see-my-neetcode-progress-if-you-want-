#updat every value in my sql column dept_code in employees

UPDATE employees
SET dept_code = FLOOR(1 + RAND() * 10);
