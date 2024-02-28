### GLOSSARY again but with a for loop printing keys and values
vintage_words = {
    "thrice" : "three times",
    "starrify" : "decorate with stars",
    "nyctophilia":  "love of darkness or the night ",
    "candor" : "honest expression",
    "serendipity" : "string of events that leads to a positive outcome"
    }

for word, meaning in vintage_words.items():
    print(f"\nword: {word}")
    print(f"meaning: {meaning}\n")

# Adding new pairs
vintage_words["elfock"] = "hair tangled as if by elves"
vintage_words["languor"] = "a state of pleasant tiredness"

### PRONUNCIATON dictionary
pretty_words = {
    "demure": "/ dɪ'mjʊə /",
    "effervescent" : "/ˌefəˈvesənt /",
    "nefarious" :"/ nɪˈfeərɪəs/",
    "Syzygy" : "/ˈsɪzɪdʒi/"
    }

# Print keys only
print("Have a look at these words, aren't they delighful!")
for word in pretty_words.keys():
    print(word)

# Print values only
print("\nJust in case you weren't sure how to pronounce them...")
for pronunciation in pretty_words.values():
    print(pronunciation)

# Sentences with keys
for word in pretty_words.keys():
    print(f"'{word.title()}' sounds wondrous!")

# Sentences with keys and values
for word, pronunciation in pretty_words.items():
    print(f"{word.title()} is pronounced {pronunciation}.")

### POLLING and looping through dictionaries and lists
fav_languages = {
    'luna': 'spanish',
    'saoirse': 'irish',
    'louise': 'french',
    'levi': 'hebrew',
    }
poll_list = ['luna', 'saoirse', 'louise', 'levi', 'ariane', 'fiia']

for name in poll_list:
    if name in fav_languages:
        print(f"Thank you for responding, {name.title()}!")
    else: 
        print(f"Please take the poll, {name.title()}!")