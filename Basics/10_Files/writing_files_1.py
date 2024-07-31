# Writing a file with the write_text() method
from pathlib import Path

path = Path('gardening.txt')
path.write_text('I like gardening.')