# A program that prompts the employee to provide their details and prints their information
from employee_class import Employee

print("Enter 'q' at any time to quit.")

while True:
    first = input("What's your first name? ")
    if first == 'q':
        break
    last = input("What's your last name? ")
    if last == 'q':
        break
    salary = input("What's your annual salary in GBP?")
    if salary == 'q':
        break

    employee_one = Employee(first, last, salary)
    print(f"Employee details: {employee_one.first_name}, {employee_one.last_name}, {employee_one.salary}")