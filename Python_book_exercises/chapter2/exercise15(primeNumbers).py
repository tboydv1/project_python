#prime number checker
from math import sqrt
number = int(input("Input an integer "))

status = True
for i in range(number//2, number):
    if i > sqrt(number):
        print(i)
        continue
    if number % i == 0:
        status = False

if status == False:
    print("{} is not a prime number".format(number))
else:
    print("{} is a prime number".format(number))