char = input("Enter a character: ").lower()
vowel = 'aeiou'

if char in vowel:
    print("The character is a vowel.")
elif 'a' <= char <= 'z':
    print("The character is a consonant.")
else:
    print("Invalid input. Please enter a letter.")