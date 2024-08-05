## Testing the survey class with the @pytest.fixture to speed up testing

import pytest
from survey_class import AnonymousSurvey

## Define a function that will build a survey that will be used for all tests
# Apply the  fixture decorator to the function

@pytest.fixture
def language_survey():
    """A survey that will be available to ll test functions."""
    question = "What's your first language?"
    language_survey = AnonymousSurvey(question)
    return language_survey

## Define test functions
# Test function has a parameter that matches the name of a function with the @pytest.fixture decorator
# The fixture will be run automatically and the return value will be passed to the test function

def test_store_single_response(language_survey):
    """Test that a single response is stored properly."""
    language_survey.store_response("Polish")
    assert "Polish" in language_survey.responses
    
def test_store_three_responses(language_survey):
    """Test if three single responses are stored properly."""
    responses = ["Polish", "English", "Irish"]
    for response in responses:
        language_survey.store_response(response)
    
    for response in responses:
        assert response in language_survey.responses