import random
import pyttsx3
from book_data import books


def set_voice(engine):
    voices = engine.getProperty('voices')
    engine.setProperty('voice', voices[1].id)  # Select a female voice

def narrate_summary(book_title, book_summary):
    engine = pyttsx3.init()
    engine.setProperty('rate', 110)  # Slower speed
    engine.setProperty('volume', 1)
    set_voice(engine)
    print(f"\n🎙️ Narrating the summary of: {book_title}")
    engine.say(book_summary)
    engine.runAndWait()

def choose_book_category():
    print("\n📚 Choose a book category:")
    print("1. Fiction 📖")
    print("2. Self-Help 🧘‍♂️")
    print("3. Science 🌌")
    print("4. Go back to Home screen 🏠")
    
    while True:
        choice = input("\nEnter your choice (1-4): ")
        if choice == '4':
            print("Returning to Home screen...")
            return 'home'
        elif choice in ['1', '2', '3']:
            categories = ["Fiction", "Self-Help", "Science"]
            return categories[int(choice) - 1]
        else:
            print("⚠️ Invalid choice. Please enter a number between 1 and 4.")

def read_book_summary():
    category = choose_book_category()

    if category == 'home':
        return

    print(f"\n📚 You chose: {category} Books\n")
    
    book = random.choice(books[category])
    book_title = book["title"]
    book_summary = book["summary"]

    print(f"📖 *{book_title}*\n")
    print(book_summary)

    print("\nChoose an option:")
    print("1. Listen to the summary.")
    print("2. Choose another book.")
    print("3. Go back to Home screen.")

    while True:
        choice = input("\nEnter your choice (1-3): ")
        if choice == "1":
            narrate_summary(book_title, book_summary)
            finish_book_menu()
            break
        elif choice == "2":
            read_book_summary()
            break
        elif choice == "3":
            print("Returning to Home screen...")
            return
        else:
            print("⚠️ Invalid choice. Please enter a number between 1 and 3.")

def finish_book_menu():
    print("\n💖 Summary finished! What would you like to do next?")
    print("1. Choose another book.")
    print("2. Go back to the Home screen.")

    while True:
        choice = input("\nEnter your choice (1-2): ")
        if choice == "1":
            read_book_summary()
            break
        elif choice == "2":
            print("Returning to Home screen...")
            return
        else:
            print("⚠️ Invalid choice. Please enter 1 or 2.")

if __name__ == "__main__":
    read_book_summary()
