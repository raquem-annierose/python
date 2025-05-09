#Member1: Zyra

songs = {
    "1": {
                "Title": "Butter", 
                "Artist": "BTS", 
                "Album": "Butter", 
                "Year": 2021, 
                "Genre": "K-pop"
             },
    "2": {
                "Title": "Kill This Love",
                "Artist": "BLACKPINK", 
                "Album": "Kill This Love", 
                "Year": 2019, "Genre": 
                "K-pop"
             },
    "3": {
              "Title": "Ice Cream", 
              "Artist": "BLACKPINK & Selena Gomez", 
              "Album": "The Album", 
              "Year": 2020, 
              "Genre": "Pop"
             }
}

def list_all():
    if songs:
        print("\nList of Songs:")
        for song_id, details in songs.items():
            print(f"Song ID: {song_id}:")
            for key, value in details.items():
                print(f"  {key}: {value}")
            print()
    else:
        print("\nNo songs in the list.")

#Member2: Annie

def add_song():
    song_id = input("Enter song ID: ")
    if song_id in songs:
        print(f"Song ID: {song_id} already exists.")
    else:
        title = input("Enter Title: ")
        artist = input("Enter Artist: ")
        album = input("Enter Album: ")
        year = int(input("Enter Year: "))
        genre = input("Enter Genre: ")
        songs[song_id] = {
                            "Title": title, 
                            "Artist": artist, 
                            "Album": album, 
                            "Year": year, 
                            "Genre": genre
                     } 
        print(f"{title} added to the list.")

#Member3: Keith

def update_song():
    song_id = input("Enter song ID to update: ")
    if song_id in songs:
        title = input("Enter new Title: ")
        artist = input("Enter new Artist: ")
        album = input("Enter new Album: ")
        year = int(input("Enter new Year: "))
        genre = input("Enter new Genre: ")
        songs[song_id] = {
                          "Title": title, 
                          "Artist": artist, 
                          "Album": album, 
                          "Year": year, 
                          "Genre": genre
                          }
        print(f"{song_id} updated.")
    else:
        print(f"{song_id} not found.")

#Member4: Mikee

def delete_song():
    song_id = input("Enter song ID to delete: ")
    if song_id in songs:
        del songs[song_id]
        print(f"{song_id} has been removed.")
    else:
        print(f"{song_id} not found.")

#Member5: Kal

def search_song():
    search_term = input("Enter title or artist to search: ").lower()
    found = False
    for song_id, details in songs.items():
        if search_term in details["Title"].lower() or search_term in details["Artist"].lower():
            print(f"\nFound in {song_id}:")
            for key, value in details.items():
                print(f"  {key}: {value}")
            found = True
            break
    if not found:
        print("No matching song found.")

def menu():
   while True:
    # TODO(member_4:Mikee): Display choices.
    print("1: List")
    print("2: Add")
    print("3: Update")
    print("4: Delete")
    print("5: Search")
    print("6: Exit")
    

    choice = input("Enter your choice: ")

    match choice:
        case "1":
            # TODO(member_1): Implement Check Equality function.
            list_all()
        case "2":
            # TODO(member_2): Implement Odd Even Zero function.
            add_song()
        case "3":
            # TODO(member_3): Implement Highest Number function.
            update_song()
        case "4":
            # TODO(member_4): Implement Coordinate Quadrant function.
            print("Item 4 selected")
        case "5":
            # TODO(member_5): Implement Consonant or Vowel function.
            print("Item 5 selected")
        case "6":
             print("Exiting program...")
             break
        case _:
            print("Invalid choice")

menu()