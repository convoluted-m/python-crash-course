# Write a program that prompts for two numbers. Add them together and print the result. 
# Catch the ValueError if either input value is not a number, and print a friendly error message.

print("Give me two numbers andf I will add them!")

while True:
    first_number = input("First: ")
    if first_number == "q":
        break
    second_number = input("Second: ")
    if second_number == "q":
        break
    try:
        answer = int(first_number) + int(second_number)
    except ValueError:
        print("Sorry, I can't accept this input. Please don't use words, only digits.")
    else:
        print(f"This gives {answer}!")