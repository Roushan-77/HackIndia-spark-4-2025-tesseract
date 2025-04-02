def show_diet_options():
    print("\n🥗 Choose a Diet Plan:")
    print("1. Balanced Diet")
    print("2. Weight Loss Diet")
    print("3. Muscle Gain Diet")
    print("4. Vegan Diet")
    print("5. Keto Diet")
    print("6. Go Back to Home Screen")

def get_diet_plan(choice):
    diet_plans = {
        "1": {
            "name": "Balanced Diet",
            "plan": [
                "🥑 Breakfast: Oatmeal with fruits and nuts",
                "🍛 Lunch: Grilled chicken, brown rice, and steamed vegetables",
                "🍲 Dinner: Salmon with quinoa and mixed greens"
            ],
            "tips": [
                "✅ Eat a variety of nutrient-dense foods",
                "💧 Stay hydrated throughout the day",
                "🕰️ Maintain regular meal timings"
            ]
        },
        "2": {
            "name": "Weight Loss Diet",
            "plan": [
                "🥚 Breakfast: Scrambled eggs with spinach",
                "🥗 Lunch: Grilled chicken salad with olive oil dressing",
                "🍵 Dinner: Vegetable soup with grilled tofu"
            ],
            "tips": [
                "⚖️ Control portion sizes to avoid overeating",
                "🚶 Exercise regularly along with a proper diet",
                "❌ Reduce sugar and processed food intake"
            ]
        },
        "3": {
            "name": "Muscle Gain Diet",
            "plan": [
                "🍳 Breakfast: Omelet with whole wheat toast",
                "🥩 Lunch: Grilled steak with sweet potatoes",
                "🥛 Dinner: Chicken breast with brown rice and a protein shake"
            ],
            "tips": [
                "🍗 Consume high-protein meals",
                "🏋️‍♂️ Strength training is crucial for muscle growth",
                "🥤 Stay hydrated to aid muscle recovery"
            ]
        },
        "4": {
            "name": "Vegan Diet",
            "plan": [
                "🥑 Breakfast: Smoothie with almond milk, banana, and chia seeds",
                "🥗 Lunch: Quinoa salad with chickpeas and avocado",
                "🍛 Dinner: Stir-fried tofu with brown rice and vegetables"
            ],
            "tips": [
                "🌱 Ensure you get enough plant-based protein",
                "🌾 Include whole grains and legumes for fiber",
                "💊 Consider B12 supplements for overall health"
            ]
        },
        "5": {
            "name": "Keto Diet",
            "plan": [
                "🥓 Breakfast: Scrambled eggs with bacon",
                "🥑 Lunch: Avocado salad with grilled chicken",
                "🥩 Dinner: Salmon with buttered asparagus"
            ],
            "tips": [
                "🥑 Focus on healthy fats and low-carb foods",
                "🚫 Avoid sugar and high-carb foods",
                "🥩 Protein intake should be moderate, not excessive"
            ]
        }
    }

    return diet_plans.get(choice, None)

def diet_recommendation():
    while True:
        show_diet_options()
        choice = input("\nEnter your choice (1-6): ")

        if choice == "6":
            print("🏠 Returning to Home Screen...")
            return

        diet = get_diet_plan(choice)

        if diet:
            print(f"\n🍽️ **{diet['name']} Plan**")
            for meal in diet["plan"]:
                print(meal)
            
            print("\n💡 **Tips for Following This Diet:**")
            for tip in diet["tips"]:
                print(tip)

            print("\nWhat would you like to do next?")
            print("1. Choose another diet")
            print("2. Go Back to Home Screen")

            next_choice = input("\nEnter your choice (1-2): ")
            if next_choice == "2":
                print("🏠 Returning to Home Screen...")
                return
        else:
            print("⚠️ Invalid choice. Please enter a number between 1 and 6.")

if __name__ == "__main__":
    diet_recommendation()
