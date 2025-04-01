from nickname import call_name
from anylaser import mental_health_assessment
from chat_bot import chatbot
from music import play_music

def main():
    while True:
        print("\n🎵 Welcome to the Mental Health Program! ")
        print("1. Choose Nickname")
        print("2. Mental Health Analyzer")
        print("3. Chatbot")
        print("4. Music Therapy 🎶")
        print("5. Exit")

        choice = input("Please enter your choice (1-5): ")

        if choice == '1':
            print(f"\nYour nickname is: {call_name}") 
        elif choice == '2':
            mental_health_assessment()  
        elif choice == '3':
            chatbot()  
        elif choice == '4':
            play_music()  
        elif choice == '5':
            print("Exiting... Goodbye! 🌿")
            break  
        else:
            print("⚠️ Invalid choice! Please enter a number between 1 and 5.")  

if __name__ == "__main__":
    main()

