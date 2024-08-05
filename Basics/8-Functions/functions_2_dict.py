# Returning a dictionary - medieval character
def create_character(first_name, last_name):
    person = {'first': first_name, 'last': last_name}
    return person

character = create_character('jane', 'dacre')
print(character)

# Returning a dictionary - album of the year
def make_album(artist, album):
    album_info = {'artist' : artist, 'album': album}
    return album_info

entry = make_album('storry','CH III: The Come Up')
print(entry)

