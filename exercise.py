class Employee:
    def __init__(self, id, name):
        self.id = id
        self.name = name

employees = []
while True:
    var1 = input("Please enter employee name (0 to quit): ")
    if var1 == "0":
        break
    employees.append(var1)

for idx, name in enumerate(employees, start=1):
    employee = Employee(idx, name)
    print("Id:", employee.id, "Name:", employee.name)
