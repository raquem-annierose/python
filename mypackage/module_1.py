from random import randint
dice_imgs = ["1", "2", "3", "4", "5", "6"]
dice_num = randint(0, 5)
print(dice_imgs[dice_num])

pages = 0
word_per_page = 0
pages = int(input("Number of pages: "))
word_per_page == int(input("Number of words per page: "))
total_words = pages * word_per_page
print(total_words)

pages = 0
word_per_page = 0
print(f"pages: {pages}, word_per_page: {word_per_page}")
pages = int(input("Number of pages: "))
print(f"pages after input: {pages}")
word_per_page = int(input("Number of words per page: "))
print(f"word_per_page after input: {word_per_page}")
total_words = pages * word_per_page
print(total_words)
       
def greet (name):
    print(f"Hi {name}!")

