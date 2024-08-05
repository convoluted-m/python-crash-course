# Show image with matplotlib
from matplotlib import image as img
from matplotlib import pyplot as plt
plt.title("pika.jpg") 
image = img.imread("/Users/martynakosciukiewicz/Documents/source/Python-Crash-Course/Basics/6_Dictionaries/pika.jpg")
plt.imshow(image)
plt.show()

# Show image with PIL
from PIL import Image
img = Image.open("/Users/martynakosciukiewicz/Documents/source/Python-Crash-Course/Basics/6_Dictionaries/pika.jpg")
img.show()