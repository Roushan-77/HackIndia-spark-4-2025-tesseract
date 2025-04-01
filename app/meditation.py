import time

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
        if remaining % 30 == 0 or remaining <= 10:  # Show countdown every 30 seconds, then every second in last 10 sec
            print(f"⏳ Time left: {remaining} seconds...", end="\r")
        time.sleep(1)

    print("\n✨ Your meditation session is complete! Take a moment to open your eyes and feel refreshed. 💙\n")

if __name__ == "__main__":
    meditation()
