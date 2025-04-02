from nickname import call_name
from anylaser import mental_health_assessment
from chat_bot import chatbot
from story import read_story
from breathing import breathing_exercise
from meditation import meditation
from music import play_music
from book import read_book_summary

def main():
    while True:
        print("\nWelcome to the Mental Health Program! 🌿")
        print("1. Choose Nickname")
        print("2. Mental Health Analyzer")
        print("3. Chatbot")
        print("4. Listen to a Story")
        print("5. Breathing Exercise")
        print("6. Meditation Session")
        print("7. Listen to Music")
        print("8. Audio Book")
        print("9. Exit")

        choice = input("\nPlease enter your choice (1-9): ")

        if choice == '1':
            print(f"\nYour nickname is: {call_name}")  
        elif choice == '2':
            mental_health_assessment()  
        elif choice == '3':
            chatbot() 
        elif choice == '4':
            read_story()  
        elif choice == '5':
            breathing_exercise()  
        elif choice == '6':
            meditation()
        elif choice == '7':
            play_music()
        elif choice == '8':
            read_book_summary()  
        elif choice == '9':
            print("🌟 Exiting... Take care and stay strong!")
            break  
        else:
            print("⚠️ Invalid choice! Please enter a number between 1 and 9.")  

if __name__ == "__main__":
    main()