## Modifying attributes

## Define the class
class Book:
    """An attempt to represent a book."""

# Define the init() method to create an instance of the class and provide the parameters
    def __init__(self, title, author, year):
        """Initialize attributes to describe a book."""
        self.title = title
        self.author = author
        self.year = year

    def get_book_description(self):
        """Return a book description ."""
        description = (f"'{self.title}' was written by {self.author} in {self.year}.")
        return description

book = Book('The Master and Margarita', 'Mikhail Bulgakov', 1928)
print(book.get_book_description())