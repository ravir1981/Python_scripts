import json

with open("Files/quiz.json", 'r') as file:
    content = file.read()

# print(content)
data = json.loads(content)
print(type(data))

for qt in data:
    print(qt["question"])
    for index, option in enumerate(qt["options"]):
        print(index + 1, "-", option)
    choice = int(input("Enter your answer:"))
    qt["choice"] = choice

# print(data)

score = 0
for index, quest in enumerate(data):
    if quest["choice"] == quest["answer"]:
        score = score + 1
        result = "Correct Answer"
    else:
        result = "Wrong Answer"
    message = (f"{index + 1} {result} - Your Answer: {quest["choice"]}, "
               f"Correct Answer: {quest["answer"]}")
    print(message)
print("Final Score", score, "/", len(data))
