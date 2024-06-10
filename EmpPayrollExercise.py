class PayrollSystem:
    def calculate_payroll(self, employees):
        for idx, employee in enumerate(employees, start=1):
            print("Employee Payroll")
            print("================")
            print(f"Payroll for: {idx} - {employee.name}")
            print(f"- Check amount: {employee.calculate_salary()}\n")


class Employee:
    def __init__(self, name):
        self.name = name


class SalaryEmployee(Employee):
    def __init__(self, name, monthly_salary):
        super().__init__(name)
        self.monthly_salary = monthly_salary

    def calculate_salary(self):
        return self.monthly_salary


if __name__ == "__main__":
    payroll_system = PayrollSystem()
    employees = []
    while True:
        name = input("Please enter employee name (0 to quit):")
        if name == "0":
            break
        salary = int(input("Please enter salary:"))
        employee = SalaryEmployee(name, salary)
        employees.append(employee)

    payroll_system.calculate_payroll(employees)
