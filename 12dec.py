'''
WAP to print number from 1 to 50 when number is multiple of  3 print "Fizz" instead of number and
when number is multiple of 5 print "Buzz" instead of number and when number is multiple of both 3 and 5
print "FizzBuzz" instead of number.else print the number.


'''

for i in range(1,51):
    if i%3==0 and i%5==0:
        print("FizzBuzz")
    elif i%5==0:
        print("Buzz")
    elif i%3==0:
        print("Fizz")
    else:
        print(i)