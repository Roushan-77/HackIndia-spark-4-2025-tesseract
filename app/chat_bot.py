import random
from nickname import call_name
from data import responses, why_reasons, hello_responses, farewell_responses, crisis_responses, thanks_responses

def chatbot():
    print(f"\nBot: You can talk to me anytime, {call_name}. Type 'exit' when you want to end.")

    while True:
        user_input = input(f"{call_name}: ").lower()
        
        if user_input == "exit":
            print(f"Bot: Remember, you are stronger than you think! Take care {call_name}!")
            break
        
        matched = False

        for keyword in hello_responses:
            if keyword in user_input:
                print("Bot:", random.choice(hello_responses[keyword]))
                matched = True
                break

        for keyword in thanks_responses:
            if keyword in user_input:
                print("Bot:", random.choice(thanks_responses[keyword]))
                matched = True
                break
        
        for keyword in responses:
            if keyword in user_input:
                print("Bot:", random.choice(responses[keyword]))
                matched = True
                break

        for keyword in why_reasons:
            if keyword in user_input:
                print("Bot:", random.choice(why_reasons[keyword]))
                matched = True
                break

        for keyword in crisis_responses:
            if keyword in user_input:
                print("Bot:", random.choice(crisis_responses[keyword]))
                matched = True
                break
        
        for keyword in farewell_responses:
            if keyword in user_input:
                print("Bot:", random.choice(farewell_responses[keyword]))
                matched = True
                break
        
        if not matched:
            print("Bot:", random.choice(responses["default"]))
