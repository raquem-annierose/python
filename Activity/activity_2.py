numbers = []
occurence = int(input("Enter the range of the list: "))

for i in range(occurence):
    numbers.append(int(input(f"Enter number {i + 1} value: ")))

print(numbers)

for idx, num in enumerate(numbers):
    print(f"{idx + 1}. {num}")

print("Alternate elements:")
for idx in range(0, len(numbers), 2):
    print(f"{idx + 1}. {numbers[idx]}")

print("Program end.")