def char_occur():
    dict_word = {}
    word = input("Enter a word: ").lower()

    for char in word:
       
        if char in dict_word:
            dict_word[char] += 1
        else:
            dict_word[char] = 1
     
    print(f"Character frequencies in {word}: {dict_word}")

char_occur()