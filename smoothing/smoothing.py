from PIL import Image

img = Image.open("cat.jpeg")
grayscale_image = img.convert('L')
grayscale_image.save('grayscale-cat.jpeg')
smoothed_image = grayscale_image

width, height = grayscale_image.size
filter = [1,1,1,1,1,1,1,1,1]

for i in range(1, width - 1):
    for j in range(1, height - 1):
        new_value = 0
        filter_counter = 0
        for k in range(i - 1, i + 2):
            for l in range(j - 1, j + 2):
                new_value += grayscale_image.getpixel((k,l)) * filter[filter_counter]
                filter_counter += 1
        new_value = int(new_value/9)
        smoothed_image.putpixel((i,j), new_value)

smoothed_image.save("smoothed-cat.jpeg")

