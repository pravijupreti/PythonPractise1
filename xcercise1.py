# Exercise

def my_split(sentence, sep):
    lst = []
    tmp = ''
    for c in sentence:
        if c == sep:
            lst.append(tmp)
            tmp = ''
        else:
            tmp += c
    if tmp:
        lst.append(tmp)

    return (lst)


def my_join(lst, sep):
    mystr = ''
    for elem in lst[0:-1]:
        mystr += str(elem) + str(sep)
    mystr += str(lst[-1])

    return (mystr)


class Employee:
    def __init__(self, id, name):
        self.id = id
        self.name = name


class SalaryEmployee(Employee):
    def __init__(self, id, name, monthly_salary):
        super().__init__(id, name)
        self.monthly_salary = monthly_salary

    def calculate_payroll(self):
        return self.monthly_salary


while True:
    print(
        "(1) Add employee to employees\n(2) Write employees to file\n(3) Read employees from file\n(4) Print employees\n(0) Quit\n")
    selection = int(input("Please select one: "))
    if selection == 1:
        salary_employees = []
        name = " "
        id = 1
        while name != '0':
            name = str(input("Please enter employee name (0 to quit):"))
            if name != '0':
                try:
                    salary = int(input("Please enter salary:"))
                except:
                    salary = 0
                salary_employees.append(SalaryEmployee(id, name, salary))
                id += 1

    elif selection == 2:
        with open("salary_employee.txt", "w") as file:
            for employee in salary_employees:
                file.write(f"{employee.id},{employee.name},{employee.monthly_salary}\n")
        print(len(salary_employees), " employee(s) added to salary_employee.txt")
        id += len(salary_employees)
    elif selection == 3:
        salary_employees = []
        with open("salary_employee.txt", "r") as file:
            for line in file:
                id, name, salary = line.strip().split(',')
                salary_employees.append(SalaryEmployee(int(id), name, int(salary)))
                file.close()
        print(len(salary_employees), "employee(s) read from salary_employee.txt")

    elif selection == 4:
        for employee in salary_employees:
            print("Id:", employee.id, "Name:", employee.name, "Salary:", employee.monthly_salary)

    elif selection == 0:
        print("Service shutting down, thank you.")
        break
    else:
        print("Incorrect selection.")
