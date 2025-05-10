from my_module import greet, pi
import math 
import datetime
import os

directory = os.getcwd()
print(directory)
#environment variables


date_today = datetime.date.today()
time_now = datetime.datetime.now().time()
print(date_today)
print(time_now)

sqrt_val = math.sqrt(64)
pi_const = math.pi
print(sqrt_val)
print(pi_const)

print(pi)
greet()

print ('Compilation of exercises')
print ('Exercise 1')
print ('Exercise 2')    




choices = int(input("Enter a number between 1 and 10: "))

if choices == 1:
      greet()
elif choices == 2:
     print(pi)
else:
        print("Invalid choice")

