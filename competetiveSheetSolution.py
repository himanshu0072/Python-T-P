'''
1. Sum of Digits: Write a function that takes an integer as input and returns the sum of its digits.

'''


# def sum(a, b):
#     sum = a + b
#     return sum
# a = int(input("Enter value of A:"))
# b = int(input("Enter value of B:"))

# print(f"The sum of {a} and {b} is {sum(a,b)}")


'''

2.Factorial Calculation: Create a function to calculate the factorial of a given number.

'''

# approach without using recurusion


# def factorial(n):
#     fact = 1
#     for i in range(1, n):
#         fact = fact + fact * i
#     return fact


# n = int(input("Enter a number to calculate factorial:"))
# print(f"The factorial of {n} is {factorial(n)}")

'''

3. Reverse a String: Write a program that reverses a given string.

'''


def reverseString(string):
    return string[::-1]


string = input("Enter a string you want to reverse:")
print(f"Reversed String = {reverseString(string)}")
