## Using a function with a while loop
def make_album(artist, album):
    album_info = f"{artist} {album}"
    return album_info.title()

while True:
    print("So, let's vote for the best album of the year!")
    print("(enter 'q' at any time to quit)")
    
    artist_name = input("So, what's the artist's name? ")
    if artist_name == 'q':
        break
    album_title = input("And the album's name? ")
    if album_title == 'q':
        break

    formatted_album_info = make_album(artist_name, album_title)
    print(f"\nYou voted for, {formatted_album_info}!")