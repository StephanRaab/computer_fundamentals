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

    @classmethod
    def set_raise_amt(cls, amount):
        cls.raise_amount = amount

emp1 = Employee("John", "Doe", 42000)
emp2 = Employee("Steve", "Smith", 52000)

Employee.set_raise_amt(1.05)

emp2.set_raise_amt(1.02)

print(emp1.pay)
emp1.give_raise()
print(emp1.pay)
print(emp2.pay)
emp2.give_raise()
print(emp2.pay)
