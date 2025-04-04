songs = {
    "Song1": {"Title": "Butter", "Artist": "BTS", "Album": "Butter", "Year": 2021, "Genre": "K-pop"},
    "Song2": {"Title": "Kill This Love", "Artist": "BLACKPINK", "Album": "Kill This Love", "Year": 2019, "Genre": "K-pop"},
    "Song3": {"Title": "Ice Cream", "Artist": "BLACKPINK & Selena Gomez", "Album": "The Album", "Year": 2020, "Genre": "Pop"}
}

def list_all():
    if songs:
        print("\nList of Songs:")
        for song_id, details in songs.items():
            print(f"{song_id}:")
            for key, value in details.items():
                print(f"  {key}: {value}")
            print()
    else:
        print("\nNo songs in the list.")

def add_song():
    song_id = input("Enter song ID: ")
    if song_id in songs:
        print(f"{song_id} already exists.")
    else:
        title = input("Enter Title: ")
        artist = input("Enter Artist: ")
        album = input("Enter Album: ")
        year = int(input("Enter Year: "))
        genre = input("Enter Genre: ")
        songs[song_id] = {"Title": title, "Artist": artist, "Album": album, "Year": year, "Genre": genre}
        print(f"{title} added to the list.")

def update_song():
    song_id = input("Enter song ID to update: ")
    if song_id in songs:
        title = input("Enter new Title: ")
        artist = input("Enter new Artist: ")
        album = input("Enter new Album: ")
        year = int(input("Enter new Year: "))
        genre = input("Enter new Genre: ")
        songs[song_id] = {"Title": title, "Artist": artist, "Album": album, "Year": year, "Genre": genre}
        print(f"{song_id} updated.")
    else:
        print(f"{song_id} not found.")

def delete_song():
    song_id = input("Enter song ID to delete: ")
    if song_id in songs:
        del songs[song_id]
        print(f"{song_id} has been removed.")
    else:
        print(f"{song_id} not found.")

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
        print("\nSongs Menu")
        print("1. List All")
        print("2. Add")
        print("3. Update")
        print("4. Delete")
        print("5. Search")
        print("6. Exit")
        
        choice = input("Choose an option: ")
        
        if choice == "1":
            list_all()
        elif choice == "2":
            add_song()
        elif choice == "3":
            update_song()
        elif choice == "4":
            delete_song()
        elif choice == "5":
            search_song()
        elif choice == "6":
            print("Exiting the program.")
            break
        else:
            print("Invalid option. Please choose again.")

menu()