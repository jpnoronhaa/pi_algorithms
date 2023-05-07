from PIL import Image

img = Image.open("berries.jpeg")
grayscale_image = img.convert('L')
grayscale_image.save('grayscale-berries.jpeg')

second_image = grayscale_image

width, height = grayscale_image.size
second_filter = [[-1,0,1],[-2,0,2],[-1,0,1]]

for i in range(1, width - 2):
    for j in range(1, height - 2):
        second_image_new_value = 0

        for k in range(3):
            for l in range(3):
                second_image_new_value += grayscale_image.getpixel((k+i,l+j)) * second_filter[k][l]

        if (second_image_new_value < 0): 
            second_image_new_value = 0

        second_image.putpixel((i,j), second_image_new_value)

second_image.save("second-sobel-berries.jpeg")