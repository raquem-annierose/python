def stats(numbers):
    total = sum(numbers)
    count = len(numbers)
    average = total / count
    return total, count, average  # Returns a tuple

result = stats([10, 20, 30])
print(result)  # Output: (60, 3, 20.0)