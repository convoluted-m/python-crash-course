# Storing and loading data using the json module

from pathlib import Path
import json

numbers = [1, 2, 3]
# Store data with json.dumps()
path = Path("numbers.json")
contents = json.dumps(numbers)
path.write_text(contents)



