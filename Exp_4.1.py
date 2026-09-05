#Playlist Manager
import random
import os

FILENAME = "playlist.txt"

def playlist_app():
    songs = []

    if os.path.exists(FILENAME):
        with open(FILENAME, "r") as f:
            songs = [line.strip() for line in f.readlines()]

    while True:
        print("\n----- PLAYLIST MANAGER -----")
        print("1. View\n2. Add\n3. Remove\n4. Shuffle\n5. Exit")
        choice = input("Select an option (1-5): ")

        if choice == "1":
            print("\nYour songs:\n")
            if songs:
                for s in songs:
                    print("-", s)
            else:
                print("Playlist is empty.")

        elif choice == "2":
            new_song = input("Enter a song name: ")
            songs.append(new_song)
            print("Song added to your playlist!")

        elif choice == "3":
            rem_song = input("Enter the song name to remove: ")
            if rem_song in songs:
                songs.remove(rem_song)
                print("Song removed from your playlist.")
            else:
                print("ERROR: Song not found in the list.")

        elif choice == "4":
            random.shuffle(songs)
            print("Songs shuffled successfully.")

        elif choice == "5":
            with open(FILENAME, "w") as f:
                for s in songs:
                    f.write(s + "\n")
            print("Playlist saved.")
            break

        else:
            print("INVALID CHOICE")

playlist_app()