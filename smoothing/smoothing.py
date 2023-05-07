from PIL import Image

img = Image.open("cat.jpeg")
grayscale_image = img.convert('L')
grayscale_image.save('grayscale-cat.jpeg')
smoothed_image = grayscale_image

width, height = grayscale_image.size
filter = [[1,1,1],[1,1,1],[1,1,1]]

for i in range(1, width - 2):
    for j in range(1, height - 2):
        new_value = 0
        for k in range(3):
            for l in range(3):
                new_value += grayscale_image.getpixel((k+i,l+j)) * filter[k][l]
        new_value = int(new_value/9)
        smoothed_image.putpixel((i,j), new_value)

smoothed_image.save("smoothed-cat.jpeg")

