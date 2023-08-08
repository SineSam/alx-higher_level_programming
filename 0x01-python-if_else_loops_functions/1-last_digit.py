#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
lastDigit = number % 10

if lastDigit > 5:
    print("{} and is greater than 5".format(lastDigit))
elif lastDigit == 0:
    print("{} and is zero".format(lastDigit))
elif lastDigit < 6 and lastDigit != 0:
    print("{} and is less than 6 and not 0".format(lastDigit))
