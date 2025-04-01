import random
import time
from stories_data import stories


def choose_category():
    """Allows the user to choose a category of stories"""
    print("\n📖 Choose a type of story you’d like to hear:")
    print("1. Inspirational ✨")
    print("2. Comforting 🤗")
    print("3. Personal Growth 🌱")
    print("4. Acts of Kindness 💖")
    
    while True:
        choice = input("\nEnter your choice (1-4): ")
        if choice in ['1', '2', '3', '4']:
            categories = ["Inspirational", "Comforting", "Personal Growth", "Acts of Kindness"]
            return categories[int(choice) - 1]
        else:
            print("⚠️ Invalid choice. Please enter a number between 1 and 4.")

def read_story():
    """Displays a random story from the chosen category"""
    category = choose_category()
    print(f"\n📚 You chose: {category} Stories\n")
    
    story = random.choice(stories[category])
    
    print(f"📖 *{story['title']}*\n")
    print(story["content"])
    
    print("\n💙 Hope this story brings you some comfort! Would you like to hear another? (yes/no)")
    choice = input("> ").lower()
    
    if choice == "yes":
        read_story()
    else:
        print("🌟 Thank you for reading! Remember, your story is still being written. Keep going! 💫")

if __name__ == "__main__":
    read_story()