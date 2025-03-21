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

    match choice:
        case "1":
            # TODO(member_2): Implement Check Equality function.
            print("Item 1 selected")
        case "2":
            # TODO(member_3): Implement Odd Even Zero function.
            print("Item 2 selected")
        case "3":
            # TODO(member_4): Implement Highest Number function.
            print("Item 3 selected")
        case "4":
            # TODO(member_5): Implement Coordinate Quadrant function.
            print("Item 4 selected")
        case "5":
            # TODO(member_6): Implement Consonant or Vowel function.
            print("Item 5 selected")
        case "6":
            # TODO(member_7): Implement Sum Two Digits function.
            print("Item 6 selected")
        case "7":
            print("Exiting program...")
            break
        case _:
            print("Invalid choice")
