def fibonacci_sequence(n):
    a, b = 0, 1
    sequence = []
    for _ in range(n):
        sequence.append(a)
        a, b = b, a + b
    return f"Fibonacci sequence: {' '.join(map(str, sequence))}"

def is_armstrong_number(num):
    digits = len(str(num))
    sum_of_digits = sum(int(digit) ** digits for digit in str(num))
    if sum_of_digits == num:
        return f"{num} is an Armstrong number."
    else:
        return f"{num} is not an Armstrong number."

def sum_of_multiples(limit, multiple):
    total_sum = sum(num for num in range(1, limit+1) if num % multiple == 0)
    return f"Sum of multiples of {multiple} up to {limit}: {total_sum}"

def reverse_string(string):
    reversed_string = string[::-1]
    return f"Reversed string: {reversed_string}"

def perfect_number_checker(num):
    divisors_sum = sum(i for i in range(1, num) if num % i == 0)
    if divisors_sum == num:
        return f"{num} is a perfect number."
    else:
        return f"{num} is not a perfect number."

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
            num = int(input("Enter a number: "))
            result = is_armstrong_number(num)
            print(result)
        elif choice == "2":
            limit = int(input("Enter the limit: "))
            multiple = int(input("Enter the multiple (e.g., 3 or 5): "))
            result = sum_of_multiples(limit, multiple)
            print(result)
        elif choice == "3":
            string = input("Enter a string: ")
            result = reverse_string(string)
            print(result)
        elif choice == "4":
            num = int(input("Enter a number: "))
            result = perfect_number_checker(num)
            print(result)
        elif choice == "5":
            n = int(input("Enter the number of terms in the Fibonacci sequence: "))
            result = fibonacci_sequence(n)
            print(result)
        elif choice == "6":
            print("Exiting...")
            break
        else:
            print("Invalid choice, try again!")

if __name__ == "__main__":
    main()
