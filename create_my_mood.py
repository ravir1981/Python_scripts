# Program written using Context Manager

date = input("Enter today's date:")
mood = input("Rate your mood:")
thoughts = input("Enter your mood: \n")

with open(f"MyMood/{date}.txt", 'w') as file:
    file.write(f"My Mood is rated at {mood}" + "\n")
    file.write(f"My though are \"{thoughts}\"" + 2 * "\n")
    file.write("I am at my Home - Avon")

