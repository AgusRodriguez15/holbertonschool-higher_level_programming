#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
last_digit = number % 10
number2 = abs(number)
#print(number2)
if last_digit > 5:
    print(f"Last digit of {number} is {last_digit} and is greater than 5")
    if number < 0:
        number2 % 10    
        print(number2)   
