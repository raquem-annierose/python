def print_values_only(**kwargs):
    for value in kwargs.values():
        print(value)

print_values_only(name="Leo", age=21, country="Philippines")