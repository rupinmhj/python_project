'''To resize an image, we use Pillow library(PIL)'''
from PIL import Image

image=Image.open("rupin.jpg")
print(image.width)
print(image.height)
new_width=int(image.width*0.2)
new_height=int(image.height*0.2)

print(new_width)
print(new_height)
resized_image=image.resize((new_width,new_height))

resized_image.save("resized_rrupin.jpg")

