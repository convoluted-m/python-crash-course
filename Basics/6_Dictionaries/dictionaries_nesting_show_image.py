# define a nested dictionary
characters = {
    'pika' : {
        'colour' : 'yellow',
        'pic' : '/Users/martynakosciukiewicz/Documents/source/Python-Crash-Course/Basics/6_Dictionaries/pika.jpg'
    },
    'muzzy' : {
        'colour' : 'green',
        'pic' : '/Users/martynakosciukiewicz/Documents/source/Python-Crash-Course/Basics/6_Dictionaries/muzzy.jpg'
    }
}

# define function to display an image  passing the image path as an argument
def image_display(image_path):
    from PIL import Image
    img = Image.open(image_path)
    img.show()

# # call the display image function and show the picture of pikachu
# image_display(characters['pika']['pic'])

# # call the display image function and show the picture of muzzy
# image_display(characters['muzzy']['pic'])

# loop through the dictionary and display images of all characters
for character, character_info in characters.items():
    print("Colour:" + characters[character]['colour'])
    print("Here goes the pic:")
    image_display(characters[character]['pic'])