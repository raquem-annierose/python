# Kirby Consultado   DIT 2-1
import os
os.system('cls')

info = []
print("Enter your informations.\n")

print("Name")
name = input(" | ")
info.append(name)

print("Age")
age = int(input(" | "))
info.append(age)

print("Address")
address = input(" | ")
info.append(address)

print("Email")
email = input(" | ")
info.append(email)

print("\nYour informations.\n")
print(f"Name: {info[-4]}")
print(f"Age: {info[-3]}")
print(f"Address: {info[-2]}")
print(f"Email: {info[-1]}")

print("\nYour informations in loop.\n")
ctr = 0
for infos in info:
    print(f"{ctr + 1}. {info[ctr]}")
    ctr += 1

print("\nProgram end.")