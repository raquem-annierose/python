def main():
    numbers = [int(input(f"Enter number {i}: ")) for i in range(1, 11)]
    print(f"The highest value is: {max(numbers)}")

main()

def find_min():
    numbers = [int(input(f"Enter number {i}: ")) for i in range(1, 5)]
    print(f"The lowest value is: {min(numbers)}")

find_min()