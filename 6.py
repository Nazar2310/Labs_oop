
class Employee:
    raise_amount = 2.55
    num_of_employees = 0

    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first + '.' + last + 'company.com'

        Employee.num_of_employees += 1

    def fullname(self):
        return '{} {}'.format(self.first, self.last)

    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amount)


employee = Employee('Teddy', 'Bear', 5000)
employee_s = Employee('Taylor', 'Twitch', 150)

employee.apply_raise()

# бібліотеки з класу
print('Info from Employee - ', employee.__dict__)
print(Employee.__dict__)

# заміна показника
employee.raise_amount = 3.55
print(employee.raise_amount)
print('count of employees = ', Employee.num_of_employees)