number = int(input("Enter a number: "))

if number % 3 == 0 and number % 5 == 0: 
   print("Bigyan ng jacket!") 
elif number % 3 == 0:
   print("Hep! Hep!")
elif number % 5 == 0: 
    print("Horaaay!")
else:
    print(f"{number} Tawsan")