inputted_number = int(input("Enter a number: "))

if inputted_number % 3 == 0 and inputted_number % 5 == 0:
    print("Bigyan ng jacket!")
elif inputted_number % 3 == 0:
    print("Hep! Hep!")
elif inputted_number % 5 == 0:
    print("Horaaay!")
else:
    print(f"{inputted_number} Tawsan")