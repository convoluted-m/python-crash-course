from pathlib import Path
import json

username = input("What's your name? ")

path = Path("username.json")
contents = json.dumps(username)
path.write_text(contents)

print(f"We will remember your name when you're back, {username}!")