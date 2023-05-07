from PIL import Image

img = Image.open("kid.jpeg")
grayscale_image = img.convert('L')
grayscale_image.save('grayscale-kid.jpeg')

third_image = grayscale_image

width, height = grayscale_image.size
third_filter = [[1,1,1],[1,-8,1],[1,1,1]]

for i in range(1, width - 2):
    for j in range(1, height - 2):
        third_image_new_value = 0

        for k in range(3):
            for l in range(3):
                third_image_new_value += grayscale_image.getpixel((k+i,l+j)) * third_filter[k][l]

        if (third_image_new_value < 0): 
            third_image_new_value = 0

        third_image.putpixel((i,j), third_image_new_value)

third_image.save("third-laplacian-kid.jpeg")