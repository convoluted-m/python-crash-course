# Testing the survey class

# Import the class to test
from survey_class import AnonymousSurvey

## Test if one answer is stored in the survey's responses
# Define the test function 
def test_store_single_response():
    """Test if a single response is stored properly."""
    question = "What's your first language?"
    # Create an instance of the class
    language_survey = AnonymousSurvey(question)
    # Store a single response using the survey method
    language_survey.store_response('Polish')
    # Verify the reponseby  asserting that it is in the responses list
    assert 'Polish' in language_survey.responses

## Test if three responses are stored correctly
# Define the test function
def test_three_responses():
    """Test that three individual responses are storec correctly."""
    question = "What is your first language?"
    # Create an instance of the class
    language_survey = AnonymousSurvey(question)
    # define a list containing three different responses
    responses = ["Polish", "English", "Irish"]
    for response in responses:
        language_survey.store_response(response)
    for response in responses:
        assert response in language_survey.responses
