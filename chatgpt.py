class Employee:
    def __init__(self, emp_name, emp_id, emp_salary, emp_department):
        self.emp_name = emp_name
        self.emp_id = emp_id
        self.emp_salary = emp_salary
        self.emp_department = emp_department

    def emp_assign_department(self, new_department):
        self.emp_department = new_department
        print(f"Department changed to {new_department} for {self.emp_name}")

    def print_employee_details(self):
        print(f"Employee Name: {self.emp_name}")
        print(f"Employee ID: {self.emp_id}")
        print(f"Employee Salary: ${self.emp_salary}")
        print(f"Employee Department: {self.emp_department}")

    def calculate_emp_salary(self, salary, hours_worked):
        if hours_worked > 50:
            overtime_hours = hours_worked - 50
            overtime_amount = overtime_hours * (salary / 50)
            total_salary = salary + overtime_amount
            return total_salary
        else:
            return salary

# Sample Employee Data
employee_data = [
    ("ADAMS", "E7876", 50000, "ACCOUNTING"),
    ("JONES", "E7499", 45000, "RESEARCH"),
    ("MARTIN", "E7900", 50000, "SALES"),
    ("SMITH", "E7698", 55000, "OPERATIONS")
]



# Calculating salary with overtime
salary = employees[3].calculate_emp_salary(50000, 55)
print(f"MARTIN's salary with overtime: ${salary}")
