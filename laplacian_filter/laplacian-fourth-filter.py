from PIL import Image

img = Image.open("kid.jpeg")
grayscale_image = img.convert('L')
grayscale_image.save('grayscale-kid.jpeg')

fourth_image = grayscale_image

width, height = grayscale_image.size
fourth_filter = [[-1,-1,-1],[-1,8,-1],[-1,-1,-1]]

for i in range(1, width - 2):
    for j in range(1, height - 2):
        fourth_image_new_value = 0

        for k in range(3):
            for l in range(3):
                fourth_image_new_value += grayscale_image.getpixel((k+i,l+j)) * fourth_filter[k][l]

        if (fourth_image_new_value < 0): 
            fourth_image_new_value = 0

        fourth_image.putpixel((i,j), fourth_image_new_value)

fourth_image.save("fourth-laplacian-kid.jpeg")