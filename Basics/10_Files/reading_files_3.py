# Absolute path - from the root
# /Users/martynakosciukiewicz/Documents/source/...
from pathlib import Path

path = Path('/Users/martynakosciukiewicz/Documents/source/python-crash-course/Basics/Text_Files/harjo_poem.txt')

harjo_poem_contents = path.read_text()
print(harjo_poem_contents)