# A class that helps administer anonymous survey responses

# Define the class
class AnonymousSurvey:
    """Collect anonymous answers to a survey question."""

    # Create a new instance of the class and initialize the class attributes
    def __init__(self, question):
        """Store the survey question and prepare to store responses."""
        self.question = question
        self.responses = []
    
    # Define other methods
    def show_question(self):
        """Show the survey question."""
        print(self.question)
    
    def store_response(self, new_response):
        """Store a single response to the survey."""
        self.responses.append(new_response)
    
    def show_results(self):
        """Show all responses."""
        print("Survey results: ")
        for response in self.responses:
            print(f"- {response}")