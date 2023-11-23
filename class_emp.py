class Employee:
    def __init__(self, emp_name, emp_id, emp_salary, emp_department):
        self.emp_name = emp_name
        self.emp_id = emp_id
        self.emp_salary = emp_salary
        self.emp_department = emp_department
    #Function employee_details
    #print employee
    def print_employee_details(self):
        print(f"Employee Name: {self.emp_name}")
        print(f"Employee ID: {self.emp_id}")
        print(f"Employee Salary: ${self.emp_salary}")
        print(f"Employee Department: {self.emp_department}")
    #Function emp_assign_department
    #change the department for employee
    def emp_assign_department(self, new_department):
        self.emp_department = new_department
        print(f"Department changed to {new_department} for {self.emp_name}")
    #Function calculate_emp_salary
    #overtime
    def calculate_emp_salary(self, hours_worked):
        if hours_worked > 50:
            overtime_hours = hours_worked - 50
            overtime_amount = overtime_hours * (self.emp_salary / 50)
            total_salary = self.emp_salary + overtime_amount
            return total_salary
        else:
            return self.emp_salary
    
#employee
emp1 = Employee("ADAMS", "E7876", 50000, "ACCOUNTING")
emp2 = Employee("JONES", "E7499", 45000, "RESEARCH")
emp3 = Employee("MARTIN", "E7900", 50000, "SALES")
emp4 = Employee("SMITH", "E7698", 55000, "OPERATIONS")

#show emloyee details
emp2.print_employee_details()

#change employee department
emp2.emp_assign_department("BOSS")

#show salary
salary = emp2.calculate_emp_salary(55)
print(f"overthime money: ${salary}")
