import time
import random
from data_anylaser import questions, suggestions, option_specific_suggestions
from nickname import call_name

def get_responses():
    """Gets and validates user inputs for all multiple-choice questions at once."""
    responses = []
    print("\n💙 Mental Health Check-in 💙")
    print("Please answer all the questions honestly and then submit.\n")

    for q_num, (question, options) in enumerate(questions.items(), start=1):
        print(f"\n({q_num}) {question}")
        for option in options:
            print(option)
    
    while len(responses) < len(questions):
        try:
            response = list(map(int, input("\nEnter your choices for all questions (space-separated, 1-4): ").split()))
            if all(1 <= r <= 4 for r in response) and len(response) == len(questions):
                responses = response
            else:
                print("⚠️ Invalid input. Make sure you enter numbers between 1-4 for all questions.")
        except ValueError:
            print("⚠️ Invalid input. Please enter only numbers between 1 and 4.")
    
    return responses

def mental_health_assessment():
    responses = get_responses()
    total_score = sum(responses)
    avg_score = total_score / len(responses)


    option_suggestions = []
    for q_num, response in enumerate(responses, start=1):
        if q_num in option_specific_suggestions:
            option_suggestions.append(random.choice(option_specific_suggestions[q_num][response]))

    
    print(f"\n💖 Dear {call_name}, you're doing great! Remember, taking care of yourself is a journey, not a destination. Here’s something for you:")
    for score_range, suggestion_list in suggestions.items():
        if score_range[0] <= avg_score <= score_range[1]:
            final_suggestion = random.choice(suggestion_list)
            print("🧡", final_suggestion)
            break

    
    if option_suggestions:
        print("\n🌿 Additional Insights Just for You:")
        for suggestion in option_suggestions:
            print(f"📝 {suggestion}")



