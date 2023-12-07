# WAP to detect youngest ages from given three ages.

age1 = int(input("Enter the first age: "))
age2 = int(input("Enter the second age: "))
age3 = int(input("Enter the third age: "))
if (age1 < age2) and (age1 < age3):
    youngest = age1
elif (age2 < age1) and (age2 < age3):
    youngest = age2
else:
    youngest = age3

print("The youngest age is", youngest)
