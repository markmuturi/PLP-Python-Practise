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



'''# Program That takes user input and creates a list of integers. Computes the sum of all integers.
def list_maker(numbers):
    var1 = []
    var1.append(numbers)
    return var1
    
print("List Maker 1.0")
numbers = (input("Enter your numbers with spaces here: ").split())
list = list_maker(numbers)
print(f"Your list is {list}")'''



'''# Create tuple cotaining 5 book names. Use a loop to print each name on a sepratrate line
book_names = ('Subtle Art', 'Jack Ryan', 'Atomic Habits', '1947')

for book in book_names:
    print(book)'''
    
    
'''# Uses a dict. to store info from user input and print the dict.
def person_dict(name, age, favColor):
    var2 = { }
    var2["name"] = name
    var2["age"] = age
    var2["color"] = favColor
    return var2
    
    

print("User Definer 1.0")
name = input("Enter your name here: ")
age = input("Enter your age here: ")
favColor = input("what's your favorite color?: ")
dict1 = person_dict(name, age, favColor)
print(f"Person Details\n: {dict1}")'''



''' # Program that accepts user input
# Creates 2 sets of integers
# Creates a new set only with common elements in both sets

print("Set Initializer & Intersector 1.0")
print("Program Started Successfully!")

numbers1 = input("Enter any random digits (0-9) with spaces. Make some similar (: : ").split()
numbers2 = input("Enter any random digits (0-9) with spaces. Make some similar (: : ").split()

def setCreator(numbers1, numbers2):
    A = set()
    B = set()
    
    A.update(numbers1)
    B.update(numbers2)
    
    print("Sets Successfully Created!\n")
    print(f"{A} && {B}")
    
    intersectSet = A.intersection(B)
    print(f"Your intersection is: {intersectSet}")
    
sets = setCreator(numbers1, numbers2) '''

    

     
    

         



            
