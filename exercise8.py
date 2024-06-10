import csv

class PayrollSystem:
    def calculate_payroll(self, employees):
        for employee in employees:
            print('Employee Payroll')
            print('================')
            print(f'Payroll for: {employee.id} - {employee.name}')
            print(f'- Check amount: {employee.calculate_salary()}')
            print('')


class Employee:
    def __init__(self, id, name):
        self.id = id
        self.name = name

    def ask_name(self):
        try:
            self.name = str(input("Please enter employee name:"))
        except:
            self.name = ''


class SalaryEmployee(Employee):
    def __init__(self, id, name, monthly_salary):
        super().__init__(id, name)
        self.salary = 'M'
        self.monthly_salary = int(monthly_salary)

    def ask_salary(self):
        try:
            self.monthly_salary = int(input("Please enter monthly salary:"))
        except:
            self.monthly_salary = 0

    def calculate_salary(self):
        return self.monthly_salary


class HourlyEmployee(Employee):
    def __init__(self, id, name, hour_rate, hours_worked):
        super().__init__(id, name)
        self.salary = 'H'
        self.hour_rate = int(hour_rate)
        self.hours_worked = int(hours_worked)

    def ask_salary(self):
        try:
            self.hours_worked = int(input("Please enter hours worked:"))
            self.hour_rate = int(input("Please enter hour rate:"))
        except:
            self.hour_rate = 0
            self.hours_worked = 0

    def calculate_salary(self):
        return self.hour_rate * self.hours_worked


class CommissionEmployee(SalaryEmployee):
    def __init__(self, id, name, monthly_salary, commission):
        super().__init__(id, name, monthly_salary)
        self.salary = 'C'
        self.commission = int(commission)

    def ask_salary(self):
        try:
            self.monthly_salary = int(input("Please enter monthly salary:"))
            self.commission = int(input("Please enter commission:"))
        except:
            self.monthly_salary = 0
            self.commission = 0

    def calculate_salary(self):
        return super().calculate_salary() + self.commission


employees = []
id_counter = 1

while True:
    print("(1) Add employee to employees\n(2) Write employees to file\n(3) Read employees from file\n(4) Print payroll\n(0) Quit\n")
    selection = int(input("Please select one: "))
    if selection == 1:
        while True:
            salarytype = int(input("Please enter salary type:\n(1) monthly\n(2) hourly\n(3) commission\n(0) Quit\n"))
            if salarytype == 1:
                employee = SalaryEmployee(id_counter, '', 0)
                employee.ask_name()
                employee.ask_salary()
                employees.append(employee)
                id_counter += 1
            elif salarytype == 2:
                employee = HourlyEmployee(id_counter, '', 0, 0)
                employee.ask_name()
                employee.ask_salary()
                employees.append(employee)
                id_counter += 1
            elif salarytype == 3:
                employee = CommissionEmployee(id_counter, '', 0, 0)
                employee.ask_name()
                employee.ask_salary()
                employees.append(employee)
                id_counter += 1
            elif salarytype == 0:
                break
            else:
                print("Incorrect selection.")
    elif selection == 2:

        with open("employee.csv", "w", newline='') as file:
            writer = csv.writer(file)
            for employee in employees:
                if isinstance(employee, SalaryEmployee) and not isinstance(employee, CommissionEmployee):
                    writer.writerow([employee.id, employee.name, 'M', employee.monthly_salary])
                elif isinstance(employee, HourlyEmployee):
                    writer.writerow([employee.id, employee.name, 'H', employee.hours_worked, employee.hour_rate])
                elif isinstance(employee, CommissionEmployee):
                    writer.writerow([employee.id, employee.name, 'C', employee.monthly_salary, employee.commission])
        with open("employee.csv", "r+") as file:
            lines = file.readlines()
            file.seek(0)
            file.truncate()
            for line in lines:
                if line.strip():

                    file.write(line)
        print(len(employees), " employee(s) added to employee.csv")
    elif selection == 3:
        employees = []
        with open("employee.csv", "r") as file:
            reader = csv.reader(file)
            for row in reader:
                id = int(row[0])
                name = row[1]
                salary_type = row[2]
                if salary_type == 'M':
                    monthly_salary = int(row[3])
                    employee = SalaryEmployee(id, name, monthly_salary)
                elif salary_type == 'H':
                    hours_worked = int(row[3])
                    hour_rate = int(row[4])
                    employee = HourlyEmployee(id, name, hour_rate, hours_worked)
                elif salary_type == 'C':
                    monthly_salary = int(row[3])
                    commission = int(row[4])
                    employee = CommissionEmployee(id, name, monthly_salary, commission)
                employees.append(employee)
        print(len(employees), " employee(s) read from employee.csv")
    elif selection == 4:
        payroll_system = PayrollSystem()
        payroll_system.calculate_payroll(employees)
    elif selection == 0:
        print("Service shutting down, thank you.")
        break
    else:
        print("Incorrect selection.")
