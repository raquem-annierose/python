def pythagorean_triple(a, b, c):
    if a**2 + b**2 == c**2 or a**2 + c**2 == b**2 or b**2 + c**2 == a**2:
        return "It's a Pythagorean triple!"
    else:
        return "Not a Pythagorean triple."

def leap_year_checker(year):
    if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
        return "Leap Year"
    else:
        return "Not a Leap Year"

def age_categorizer(age):
    if age <= 12:
        return "Child"
    elif age <= 17:
        return "Teen"
    elif age <= 64:
        return "Adult"
    else:
        return "Senior"

def simple_calculator(num1, operator, num2):
    if operator == '+':
        return num1 + num2
    elif operator == '-':
        return num1 - num2
    elif operator == '*':
        return num1 * num2
    elif operator == '/':
        return num1 / num2
    elif operator == '%':
        return num1 % num2
    elif operator == '//':
        return num1 // num2
    elif operator == '**':
        return num1 ** num2
    else:
        return "Invalid operator"

def grade_converter(grade):
    if grade >= 96:
        return "1.0"
    elif grade >= 94:
        return "1.25"
    elif grade >= 91:
        return "1.5"
    elif grade >= 89:
        return "1.75"
    elif grade >= 86:
        return "2.0"
    elif grade >= 83:
        return "2.25"
    elif grade >= 80:
        return "2.5"
    else:
        return "Fail"

def password_strength_checker(password):
    if len(password) < 6:
        return "Too short"
    elif password.isalpha() or password.isdigit():
        return "Weak password"
    else:
        return "Strong password"

def triangle_type(a, b, c):
    if a == b == c:
        return "Equilateral triangle"
    elif a == b or a == c or b == c:
        return "Isosceles triangle"
    else:
        return "Scalene triangle"

def bmi_calculator(weight, height):
    bmi = weight / (height ** 2)
    if bmi < 18.5:
        return f"Your BMI is {bmi:.2f}, Underweight"
    elif bmi < 24.9:
        return f"Your BMI is {bmi:.2f}, Normal weight"
    elif bmi < 29.9:
        return f"Your BMI is {bmi:.2f}, Overweight"
    else:
        return f"Your BMI is {bmi:.2f}, Obese"

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
            # Example: Pythagorean Triple with arguments
            result = pythagorean_triple(3, 4, 5)
            print(result)
        elif choice == "2":
            # Example: Leap Year Checker with argument
            result = leap_year_checker(2024)
            print(result)
        elif choice == "3":
            # Example: Age Categorizer with argument
            result = age_categorizer(25)
            print(result)
        elif choice == "4":
            # Example: Simple Calculator with arguments
            result = simple_calculator(5, '+', 3)
            print(result)
        elif choice == "5":
            # Example: Grade Converter with argument
            result = grade_converter(92)
            print(result)
        elif choice == "6":
            # Example: Password Strength Checker with argument
            result = password_strength_checker("P@ssw0rd")
            print(result)
        elif choice == "7":
            # Example: Triangle Type Identifier with arguments
            result = triangle_type(3, 4, 5)
            print(result)
        elif choice == "8":
            # Example: BMI Calculator with arguments
            result = bmi_calculator(70, 1.75)
            print(result)
        elif choice == "9":
            print("Exiting...")
            break
        else:
            print("Invalid choice, try again!")

if __name__ == "__main__":
    main()
