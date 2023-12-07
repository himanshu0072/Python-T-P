# A company wants to increase salary by 10% if they complete more than 5 years in the company.WAP to return updated salary of an employee.


salary = int(input("Enter the salary: "))
years = int(input("Enter the years: "))
if years > 5:
    salary = salary + (salary * 0.1)
    print("The updated salary is:", salary)
else:
    print("The salary is not updated")
