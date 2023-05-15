from PIL import Image

img = Image.open("plate.jpg")
bin_image = img.convert('1')
bin_image.save('bin-plate.jpg')
dilated_image = bin_image

width, height = bin_image.size
filter = [[0,0,0],[0,0,0],[0,0,0]]

for i in range(1, width - 2):
    for j in range(1, height - 2):
        
        if (bin_image.getpixel((i,j)) == filter[1][1]):
            for k in range(-1, 1):
                for l in range(-1, 1):
                    dilated_image.putpixel((i + k, j + l), filter[k+1][l+1])

dilated_image.save("dilated-plate.jpg")