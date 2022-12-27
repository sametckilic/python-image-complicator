from PIL import Image
import random
input_image = Image.open('tate38.png')

pixel_map = input_image.load()

width, height = input_image.size


for x in range(0, width):
    for y in range(0, height):
        r,g,b = input_image.getpixel((x,y))
        red = r - (x*y)%255 if r - (x*y)%255 >= 0 else r - (x*y)%255 + 255
        green = g - (x*y)%255 if g - (x*y)%255 >= 0 else g - (x*y)%255 + 255
        blue = b - (x*y)%255 if b - (x*y)%255 >= 0 else b - (x*y)%255 + 255
        pixel_map[x,y] = (red,green,blue)

input_image.save("tate"+str(random.randint(0,1000))+".png",format="png")
 