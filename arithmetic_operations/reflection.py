from PIL import Image

def reflect(img, newImg, x0, y0):
    x = -x0
    y = y0
    newImg.putpixel((x,y), img.getpixel((x0,y0)))

img = Image.open('img1.jpg')
width, height = img.size

newImg = Image.new(mode = "RGB", size = (width, height))

for i in range(width):
    for j in range(height):
        reflect(img, newImg, i, j)

newImg.save("img1-reflected.jpg")
