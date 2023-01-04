from PIL import Image
import random

input_image = Image.open('image.png')

pixel_map = input_image.load()

width, height = input_image.size


for x in range(0, width):
    for y in range(0, height):
        r,g,b,o = input_image.getpixel((x,y))
        red = ((x*y)%256 + r)%256
        green= ((x*y)%256 + g)%256
        blue = ((x*y)%256 + b)%256
        pixel_map[x,y] = (red,green,blue)

input_image.show()


