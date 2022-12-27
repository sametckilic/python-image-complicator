from PIL import Image
import random

input_image = Image.open('jamal.jpg')

pixel_map = input_image.load()

width, height = input_image.size


for x in range(0, width):
    for y in range(0, height):
        r,g,b = input_image.getpixel((x,y))
        
        pixel_map[x,y] = (((x*y)%255 + r)%255,((x*y)%255 +g)%255,((x*y)%255 +b)%255)

input_image.save("tate"+str(random.randint(0,1000))+".png",format="png")
