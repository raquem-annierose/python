
grade = int(input("Enter your grade (or type -1 to exit): "))

if grade > 96:
    print("1.0")
elif 94 <= grade <= 96:
    print("1.25")
elif 91 <= grade <= 93:
    print("1.5")
elif 88 <= grade <= 90:
    print("1.75")
elif 85 <= grade <= 87:
    print("2.0")
elif 82 <= grade <= 84:
    print("2.25")
elif 79 <= grade <= 81:
    print("2.5")
elif 76 <= grade <= 78:
    print("2.75")
elif grade == 75:
    print("3.0 (Passing)")
elif 70 <= grade <= 74:
    print("4.0 (Conditional)")
elif grade < 70:
    print("5.0 (Failed)")
else:
    print("Invalid grade")

print()  # Adds a blank line for better readability
