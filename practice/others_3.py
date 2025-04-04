def fibonacci_sequence():
    n = int(input("Enter the number of terms in the Fibonacci sequence: "))
    a, b = 0, 1
    print("Fibonacci sequence:")
    for _ in range(n):
        print(a, end=" ")
        a, b = b, a + b
    print()  # New line after the sequence


def is_armstrong_number():
    num = int(input("Enter a number: "))
    digits = len(str(num))
    sum_of_digits = sum(int(digit) ** digits for digit in str(num))
    if sum_of_digits == num:
        print(f"{num} is an Armstrong number.")
    else:
        print(f"{num} is not an Armstrong number.")


def sum_of_multiples():
    limit = int(input("Enter the limit: "))
    multiple = int(input("Enter the multiple (e.g., 3 or 5): "))
    total_sum = sum(num for num in range(1, limit+1) if num % multiple == 0)
    print(f"Sum of multiples of {multiple} up to {limit}: {total_sum}")


def reverse_string():
    string = input("Enter a string: ")
    reversed_string = string[::-1]
    print(f"Reversed string: {reversed_string}")


def perfect_number_checker():
    num = int(input("Enter a number: "))
    divisors_sum = sum(i for i in range(1, num) if num % i == 0)
    if divisors_sum == num:
        print(f"{num} is a perfect number.")
    else:
        print(f"{num} is not a perfect number.")


def main():
    while True:
        print("\nChoose an exercise:")
        print("1: Armstrong Number Checker")
        print("2: Sum of Multiples")
        print("3: Reverse String")
        print("4: Perfect Number Checker")
        print("5: Fibonacci Sequence Generator")
        print("6: Exit")
        choice = input("Enter your choice: ")
        if choice == "1":
            is_armstrong_number()
        elif choice == "2":
            sum_of_multiples()
        elif choice == "3":
            reverse_string()
        elif choice == "4":
            perfect_number_checker()
        elif choice == "5":
            fibonacci_sequence()
        elif choice == "6":
            print("Exiting...")
            break
        else:
            print("Invalid choice, try again!")


if __name__ == "__main__":
    main()
