# Program that reads a file and writes a modified version to a new file
# Asks the user for a filename and handles errors if the name doesn't exist or can't be read

with open("input1.txt", "w") as file:
    file.write("This is a new file!\n")
    file.write("This is a new file!\n")
    file.write("This is a new file!\n")
    file.write("This is a new file!\n")
    file.write("This is a new file!\n")
    file.write("This is a new file!\n")
    
with open("input1.txt", "r") as file:
    content = file.read()
    
content_upper = content.upper()
fileName = input("enter your filename here: ")

try:
    with open(f"{fileName}", "w") as file:
        file.write(content_upper + "\n")

except FileNotFoundError:
    print("Error! File not found")