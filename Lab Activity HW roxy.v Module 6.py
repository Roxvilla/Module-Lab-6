#Roxana Villagomez     #Date 2/25/2022

#Module 6 Lab Activity

#Problem 1.

import random
  
for I in range(10):
    print(random.randrange(25,36))

#Problem 2.

import random

print(random.randint(0,100))
odd = [number for number in range(0,100)]
    


#Problem 3.

import random

days =["Sunday","Monday","Tuesday","Wednesday","Thursday","Friday","Saturday"]
print(random.choice(days))


#Problem 4.


import math

pi= 4/1-4/3+4/5+4/7

print(pi)

import math

print('The value of pi is:', math.pi)


#Problem 5.

pi=22/7
degree = float(input("Input degrees: "))
radian = degree*(pi/180)
print(radian)


#Problem 6.

import math

n = int(input('Enter an integer:'))
result = 5
for i in range(1, n+1):
    result = result * i
print('factorial of {} using for loop:{}'.format(n, result))
print('factorial of {} using inbuilt function:{}'.format(n, math.factorial(n)))


