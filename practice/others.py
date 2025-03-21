def pythagorean_triple():
    a = int(input("Enter first number: "))
    b = int(input("Enter second number: "))
    c = int(input("Enter third number: "))
    if a**2 + b**2 == c**2 or a**2 + c**2 == b**2 or b**2 + c**2 == a**2:
        print("It's a Pythagorean triple!")
    else:
        print("Not a Pythagorean triple.")

def leap_year_checker():
    year = int(input("Enter a year: "))
    if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
        print("Leap Year")
    else:
        print("Not a Leap Year")

def age_categorizer():
    age = int(input("Enter your age: "))
    if age <= 12:
        print("Child")
    elif age <= 17:
        print("Teen")
    elif age <= 64:
        print("Adult")
    else:
        print("Senior")

def simple_calculator():
    num1 = float(input("Enter first number: "))
    operator = input("Enter operator (+, -, *, /, %, //, **): ")
    num2 = float(input("Enter second number: "))
    if operator == '+':
        print(num1 + num2)
    elif operator == '-':
        print(num1 - num2)
    elif operator == '*':
        print(num1 * num2)
    elif operator == '/':
        print(num1 / num2)
    elif operator == '%':
        print(num1 % num2)
    elif operator == '//':
        print(num1 // num2)
    elif operator == '**':
        print(num1 ** num2)
    else:
        print("Invalid operator")

def grade_converter():
    grade = int(input("Enter numeric grade (0-100): "))
    if grade >= 96:
        print("1.0")
    elif grade >= 94:
        print("1.25")
    elif grade >= 91:
        print("1.5")
    elif grade >= 89:
        print("1.75")
    elif grade >= 86:
        print("2.0")
    elif grade >= 83:
        print("2.25")
    elif grade >= 80:
        print("2.5")
    else:
        print("Fail")

def password_strength_checker():
    password = input("Enter password: ")
    if len(password) < 6:
        print("Too short")
    elif password.isalpha() or password.isdigit():
        print("Weak password")
    else:
        print("Strong password")

def triangle_type():
    a = int(input("Enter first side: "))
    b = int(input("Enter second side: "))
    c = int(input("Enter third side: "))
    if a == b == c:
        print("Equilateral triangle")
    elif a == b or a == c or b == c:
        print("Isosceles triangle")
    else:
        print("Scalene triangle")

def bmi_calculator():
    weight = float(input("Enter your weight (kg): "))
    height = float(input("Enter your height (m): "))
    bmi = weight / (height ** 2)
    print(f"Your BMI is {bmi:.2f}")
    if bmi < 18.5:
        print("Underweight")
    elif bmi < 24.9:
        print("Normal weight")
    elif bmi < 29.9:
        print("Overweight")
    else:
        print("Obese")

def main():
    while True:
        print("\nChoose an exercise:")
        print("1: Pythagorean Triple Checker")
        print("2: Leap Year Checker")
        print("3: Age Categorizer")
        print("4: Simple Calculator")
        print("5: Grade Converter")
        print("6: Password Strength Checker")
        print("7: Triangle Type Identifier")
        print("8: BMI Calculator")
        print("9: Exit")
        choice = input("Enter your choice: ")
        if choice == "1":
            pythagorean_triple()
        elif choice == "2":
            leap_year_checker()
        elif choice == "3":
            age_categorizer()
        elif choice == "4":
            simple_calculator()
        elif choice == "5":
            grade_converter()
        elif choice == "6":
            password_strength_checker()
        elif choice == "7":
            triangle_type()
        elif choice == "8":
            bmi_calculator()
        elif choice == "9":
            print("Exiting...")
            break
        else:
            print("Invalid choice, try again!")

if __name__ == "__main__":
    main()
