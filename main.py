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

    def checkEquality():
        # TODO(member_2): Do item 1.
        print("Item 1 selected")

    def oddEvenZero():
        # TODO(member_3): Do item 2.
        print("Item 2 selected")
    
    def highestNumber():
        # TODO(member_3): Do item 2.
        print("Item 3 selected")

    def coordinateQuadrant():
        # TODO(member_3): Do item 2.
        print("Item 4 selected")

    def consonantVowel():
        # TODO(member_3): Do item 2.
        print("Item 5 selected")

    def sumTwoDigits():
        # TODO(member_3): Do item 2.
        print("Item 6 selected")

    # Dictionary to simulate switch-case
    switch = {
        "1": checkEquality,
        "2": oddEvenZero,
        "3": highestNumber,
        "4": coordinateQuadrant,
        "5": consonantVowel,
        "6": sumTwoDigits,
        "7": lambda: print("Exiting program...")
    }

    # Execute the corresponding function
    if choice in switch:
        switch[choice]()
    else:
        print("Invalid choice")