grade = int(input("Enter your grade: "))

if grade > 96:
    print("1.0")
elif  grade >= 94:
    print("1.25")
elif grade <= 93 and grade >= 91:
    print("1.5")
elif grade <= 88 and grade >= 86:
    print("1.75")
elif grade <= 85 and grade >= 83:
    print("2.0")
elif grade <= 82 and grade >= 79:
    print("2.25")
elif grade <= 78 and grade >= 76:
    print("2.5")
elif grade <= 75 and grade >= 73:
    print("2.75")
elif grade == 75:
    print("3.0 (Passing)")
elif grade <= 75 and grade >= 71:
    print("4.0 (Conditional)")
elif grade < 70:
    print("5.0 (Failed)")
else:
    print("Invalid grade")