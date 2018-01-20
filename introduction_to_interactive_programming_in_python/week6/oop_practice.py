class Employee:
    num_of_employees = 0
    raise_amount = 1.03

    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.email = first + "." + last + "@company.com"
        self.pay = pay

        Employee.num_of_employees += 1

    def full_name(self):
        return '{} {}'.format(self.first, self.last)

    def give_raise(self):
        self.pay = int(self.pay * self.raise_amount)


emp1 = Employee("test", "user", 42000)
emp2 = Employee("test2", "user", 52000)

print(emp1.pay)
emp1.give_raise()
print(emp1.pay)
print(Employee.num_of_employees)
