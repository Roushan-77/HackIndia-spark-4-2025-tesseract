import time
import pyttsx3  

def meditation():
    """Guides the user through a relaxing meditation session."""
    print("\n🌸 Welcome to the Guided Meditation 🌸")
    print("\nTake a deep breath, relax, and choose your meditation duration.\n")
    
    while True:
        try:
            duration = int(input("🕰️ Enter meditation time in minutes (2, 5, 10): "))
            if duration in [2, 5, 10]:
                break
            else:
                print("⚠️ Please enter a valid time (2, 5, or 10 minutes).")
        except ValueError:
            print("⚠️ Invalid input. Please enter a number.")

    total_seconds = duration * 60
    print(f"\n🧘 Your {duration}-minute meditation session begins now. Close your eyes and focus on your breath...\n")

    
    for remaining in range(total_seconds, 0, -1):
        time.sleep(1)

    print("\n✨ Your meditation session is complete! Take a moment to open your eyes and feel refreshed. 💙\n")

    
    engine = pyttsx3.init()
    engine.setProperty('rate', 150) 
    engine.setProperty('volume', 1)  

  
    engine.say("Your meditation session is complete. Gently open your eyes and feel refreshed.")
    engine.runAndWait() 

if __name__ == "__main__":
    meditation()
