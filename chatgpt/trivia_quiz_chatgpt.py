import random

# Define a dictionary to store music questions and answers
music_questions = {
    "Which British band released the album 'OK Computer' in 1997?": "Radiohead",
    "Who won the Grammy for Album of the Year in 2020?": "Billie Eilish",
    "What was the first music video ever played on MTV?": "Video Killed the Radio Star"
}

# Choose a random question from the music category
question = random.choice(list(music_questions.keys()))

# Prompt the user to guess the answer
print("Here's a music trivia question:")
print(question)
user_answer = input("Enter your answer: ")

# Check if the user's answer is correct
correct_answer = music_questions[question]
if user_answer.lower() == correct_answer.lower():
    print("Correct! Well done!")
else:
    print(f"Sorry, the correct answer is {correct_answer}. Better luck next time!")