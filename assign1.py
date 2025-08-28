# Defining the function to get and parse input from the user
def get_num(prompt):
    while True:
        try:
            return float(float(input(prompt)))
        except ValueError:
            print("Error: Invalid input detected! Please enter a valid number")
    

# Calling the function and defining variables
print("Simple Calculator 1.0. Enjoy! :)")
num1 = get_num("Please Enter the first digit here: ")
num2 = get_num("Please Enter the second digit here: ")
operator = str(input("Please enter your desired operator here: "))


# Defining the calculation conditional clauses and relevant errors
try:
    if operator == "+":
        result = num1 + num2
    elif operator == "-":
        result = num1 - num2
    elif operator == "*":
        result = num1 * num2
    elif operator == "/":
        if num2 == 0:
            print("Error: No number is divisible by zero!")
        else:
            result = num1 / num2
    else:
        print("Error: Invalid Operator")
        result = None
    
    if result is not None:
        print(f"{num1} {operator} {num2} = {result}")
        
except Exception as e:
    print(f"An unexpected error has occurred: {e}")
        

