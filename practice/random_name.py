import random

def menu_display():
    print("1. Add student name")
    print("2. Print all student")
    print("3. Print random student")
    print("4. Exit")

def add_student_name(class_list):
    input_student = input("Enter student name: ")

    class_list.append(input_student)

def display_all_students(class_list):
    print(class_list)

def display_random_student(class_list):
    random_student = random.choice(class_list)

    print(random_student)

def main_menu():
    class_list = []

    while True:
        menu_display()

        choice = input("Enter your choice: ")

        if choice == "1":
            print("\n")
            add_student_name(class_list)
        elif choice == "2":
            print("\n")
            display_all_students(class_list)
        elif choice == "3":
            print("\n")
            display_random_student(class_list)
        elif choice == "4":
            print("Exiting program")
            break
        else:
            print("Invalid input")

main_menu()