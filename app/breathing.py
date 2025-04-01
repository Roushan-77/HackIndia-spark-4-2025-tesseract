import time

def breathing_exercise():
    """Guides the user through a simple breathing exercise for relaxation."""
    print("\n🧘 Welcome to the Breathing Exercise for Relaxation 🧘")
    print("\nFollow along with the prompts to calm your mind and body.\n")
    
    rounds = 3  # Number of breathing cycles
    for i in range(rounds):
        print(f"\n🌿 Round {i + 1}/{rounds} - Let's begin:")
        print("\nInhale deeply... 🫁 (4 seconds)")
        time.sleep(4)

        print("\nHold your breath... ✋ (4 seconds)")
        time.sleep(4)

        print("\nExhale slowly... 🌬️ (6 seconds)")
        time.sleep(6)

        print("\nRelax... 😌 Feel the calmness within you.")
        time.sleep(2)

    print("\n💙 Great job! How do you feel? Remember, deep breathing helps reduce stress and improves focus.\n")
    print("Would you like to do another round? (yes/no)")
    
    choice = input("> ").strip().lower()
    if choice == "yes":
        breathing_exercise()
    else:
        print("\n✨ Thank you for taking a moment to breathe! Stay calm and take care. 💙")

if __name__ == "__main__":
    breathing_exercise()