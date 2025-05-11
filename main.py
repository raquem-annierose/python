from mypackage import module_1, module_2 

module_1.greet("Annie")
module_2.say_hello()

while True:
    # TODO(member_1): Display choices.
    print("1: Check Equality")
    print("2: Odd Even Zero")
    print("3: Highest Number")
    print("4: Coordinate Quadrant")
    print("5: Consonant or Vowel")
    print("6: Sum Two Digits")
    print("7: Exit")

    choice = input("Enter your choice: ")

    def check_equality():
        # TODO(member_2): Do item 1.
        print("Item 1 selected")

    def odd_even_zero():
        # TODO(member_3): Do item 2.
        print("Item 2 selected")
    
    def highest_number():
        # TODO(member_3): Do item 2.
        print("Item 3 selected")

    def coordinate_quadrant():
        # TODO(member_3): Do item 2.
        print("Item 4 selected")

    def consonant_vowel():
        # TODO(member_3): Do item 2.
        print("Item 5 selected")

    def sum_two_digits():
        # TODO(member_3): Do item 2.
        print("Item 6 selected")

    # Dictionary to simulate switch-case
    switch = {
        "1": check_equality,
        "2": odd_even_zero,
        "3": highest_number,
        "4": coordinate_quadrant,
        "5": consonant_vowel,
        "6": sum_two_digits,
        "7": lambda: print("Exiting program...")
    }

    # Execute the corresponding function
    if choice in switch:
        switch[choice]()
    else:
        print("Invalid choice")