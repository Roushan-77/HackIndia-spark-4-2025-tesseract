import random
import pyttsx3
from stories_data import stories

def choose_category():
    print("\n📖 Choose a type of story you’d like to hear:")
    print("1. Inspirational ✨")
    print("2. Comforting 🤗")
    print("3. Personal Growth 🌱")
    print("4. Acts of Kindness 💖")
    print("5. Go back to Home screen 🏠")
    
    while True:
        choice = input("\nEnter your choice (1-5): ")
        if choice == '5':
            print("Returning to Home screen...")
            return 'home'
        elif choice in ['1', '2', '3', '4']:
            categories = ["Inspirational", "Comforting", "Personal Growth", "Acts of Kindness"]
            return categories[int(choice) - 1]
        else:
            print("⚠️ Invalid choice. Please enter a number between 1 and 5.")

def set_voice(engine):
    voices = engine.getProperty('voices')
   
    engine.setProperty('voice', voices[1].id)  

def narrate_story(story_title, story_content):
    engine = pyttsx3.init()
    engine.setProperty('rate', 150)  
    engine.setProperty('volume', 1)
    
    set_voice(engine) 
    
    print(f"\n🎙️ Narrating the story: {story_title}")
    engine.say(story_content)
    engine.runAndWait()

def read_story():
    category = choose_category()
    
    if category == 'home':
        return

    print(f"\n📚 You chose: {category} Stories\n")
    
    story = random.choice(stories[category])
    story_title = story["title"]
    story_content = story["content"]

    print(f"📖 *{story_title}*\n")
    print(story_content)

    print("\nChoose an option:")
    print("1. Listen to the story.")
    print("2. Choose another story.")
    print("3. Go back to the Home screen.")

    while True:
        choice = input("\nEnter your choice (1-3): ")
        if choice == "1":
            narrate_story(story_title, story_content)
            finish_story_menu()
            break
        elif choice == "2":
            read_story()
            break
        elif choice == "3":
            print("Returning to Home screen...")
            return
        else:
            print("⚠️ Invalid choice. Please enter a number between 1 and 3.")

def finish_story_menu():
    print("\n💖 Story finished! What would you like to do next?")
    print("1. Choose another story.")
    print("2. Go back to the Home screen.")

    while True:
        choice = input("\nEnter your choice (1-2): ")
        if choice == "1":
            read_story()
            break
        elif choice == "2":
            print("Returning to Home screen...")
            return
        else:
            print("⚠️ Invalid choice. Please enter 1 or 2.")

if __name__ == "__main__":
    read_story()
