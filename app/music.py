import webbrowser


music_playlists = {
    "Relaxation": "https://youtu.be/hlWiI4xVXKY?si=MpMG3L52FnniY7VS",  
    "Focus": "https://youtu.be/Nd76Bm3WXNc?si=zMqVEwBo32vaxvAH",  
    "Positive Vibes": "https://youtu.be/bw7bVpI5VcM?si=e85wHY3aY0S7ZEU2",  
    "Sleep": "https://youtu.be/1ZYbU82GVz4?si=ZiuLJBITczQnMH18",  
    "Instrumental": "https://youtu.be/n61ULEU7CO0?si=ynfkNQsovlDdHkPZ", 
    "random" : "https://youtu.be/9Kvf3QYCOmA?si=0Yr5CsHHWGptPIh_"
}

def play_music():
    print("\n🎶 Music Therapy: Choose a Playlist")
    print("1. Relaxation & Meditation 🧘‍♂️")
    print("2. Focus & Study 📚")
    print("3. Positive Vibes 🌞")
    print("4. Deep Sleep & Stress Relief 😴")
    print("5. Instrumental & Acoustic 🎻")
    print("6. Random Recommendation 🎲")

    choice = input("Select a category (1-6): ")

    playlist_links = list(music_playlists.values())

    if choice == '1':
        webbrowser.open(music_playlists["Relaxation"])
    elif choice == '2':
        webbrowser.open(music_playlists["Focus"])
    elif choice == '3':
        webbrowser.open(music_playlists["Positive Vibes"])
    elif choice == '4':
        webbrowser.open(music_playlists["Sleep"])
    elif choice == '5':
        webbrowser.open(music_playlists["Instrumental"])
    elif choice == '6':
        webbrowser.open(music_playlists["random"]) 
    else:
        print("⚠️ Invalid choice! Please enter a number between 1 and 6.")

if __name__ == "__main__":
    play_music()
