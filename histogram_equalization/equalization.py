from PIL import Image

img = Image.open('bird.jpeg')
grayscale_image = img.convert('L')
grayscale_image.save('grayscale-bird.jpeg')
equalized_image = grayscale_image

width, height = grayscale_image.size
pixel_qtd = width * height

equalized_value = []
gray_levels_sums = []
frequency_sum = 0

for i in range(256): gray_levels_sums.append(0)

for i in range(width):
        for j in range(height):
            gray_levels_sums[grayscale_image.getpixel((i,j))] += 1

for i in range(256):
    frequency = gray_levels_sums[i] / pixel_qtd
    frequency_sum += frequency
    equalized_value.append(round(frequency_sum * 255))

for i in range(width):
    for j in range(height):
        original_value = grayscale_image.getpixel((i,j))
        equalized_image.putpixel((i,j), equalized_value[original_value])

equalized_image.save('equalized-bird.jpeg')

