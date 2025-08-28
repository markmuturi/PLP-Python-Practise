''' Personalized Greeting App
name = str(input("What's Your name?: "))
color = str(input("What's your favorite color?: "))

print(f"Hello, {name}! Your favorite color is {color}")'''

'''# Simple Quiz Game
    # Function Definition
def quizzie(questions, choices, correct_answer):
    print(questions)
    for i, choice in enumerate(choices, 1):
        print(f"{i}. {choice}")
        
    while True:
        try:
            answer = int(input("Enter your choice(number): "))
            if 1 <= answer <= len(choices):
                return answer == correct_answer
            else:
                print("Invalid choice. Please try again.")
        except ValueError:
            print("Please enter a valid number.")
          
questions_data = [
    {
        "question": "When did the Dark Knight make its theatrical release?",
        "choices": [2008, 2005, 2012, 2025],
        "correct": 1
    },
    {
        "question": "Who voiced Po in KungFu Panda?",
        "choices": ["Jack Black", "Seth McFarlane", "David Corenswet", "Ben Affleck"],
        "correct": 1
    },
    {
        "question": "Is the F1 movie absolute dogshit?",
        "choices": ["Yes", "No"],
        "correct": 1
    }
]

for question_data in questions_data:
    is_correct = quizzie(
        question_data["question"],
        question_data["choices"],
        question_data["correct"]
    )
print("Correct!" if is_correct else "Wrong!")
print("-" * 30)'''


        
