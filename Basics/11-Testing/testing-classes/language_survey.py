#  A program that conducts a survey prompting the users about their first language and prints the survey results

# Import the survey function
from survey_class import AnonymousSurvey

# Define the survey question 
question = "What's your first language?"

# Make the survey - create an object with that question
language_survey = AnonymousSurvey(question)

# Show the question and store responses by calling the survey class methods
language_survey.show_question()
print("Enter 'q' any time you want to quit the survey.")

while True:
    response = input("Language: ")
    if response == "q":
        break
    language_survey.store_response(response)

# Show the results
print("Thank you for taking part in the survey!")
language_survey.show_results()