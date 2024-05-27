class Employee:
    def __init__(self, emp_id, emp_name, emp_salary, emp_department):
        self.emp_id = emp_id
        self.emp_name = emp_name
        self.emp_salary = emp_salary
        self.emp_department = emp_department

    def calculate_emp_salary(self, hours_worked):
        if hours_worked > 50:
            overtime = hours_worked - 50
            overtime_amount = overtime * (self.emp_salary / 50)
            total_salary = self.emp_salary + overtime_amount
        else:
            total_salary = self.emp_salary
        return total_salary

    def emp_assign_department(self, new_department):
        self.emp_department = new_department

    def print_employee_details(self):
        print(f"Employee ID: {self.emp_id}")
        print(f"Employee Name: {self.emp_name}")
        print(f"Employee Salary: ${self.emp_salary}")
        print(f"Employee Department: {self.emp_department}")

# Sample Employee Data
employees = [
    Employee("E7876", "ADAMS", 50000, "ACCOUNTING"),
    Employee("E7499", "JONES", 45000, "RESEARCH"),
    Employee("E7900", "MARTIN", 50000, "SALES"),
    Employee("E7698", "SMITH", 55000, "OPERATIONS")
]

# Usage
for emp in employees:
    emp.emp_assign_department("IT")  # Changing department using emp_assign_department method
    emp.print_employee_details()  # Printing employee details using print_employee_details method
    print("Total Salary with overtime:", emp.calculate_emp_salary(55))  # Calculating salary with overtime
