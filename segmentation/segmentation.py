from PIL import Image

img = Image.open('lord_shen.jpg')
grayscale_image = img.convert('L')
grayscale_image.save('grayscale-lord_shen.jpg')
width, height = grayscale_image.size

def getThreshold(image, width, height):
    counter = 0
    sum = 0
    for i in range(0, width - 1):
        for j in range(0, height - 1):
            counter += 1
            sum += image.getpixel((i,j))
    threshold = sum / counter
    return threshold

def segment(image, threshold, width, height):
    bin_img = image
    for i in range(0, width - 1):
        for j in range(0, height - 1):
            if (image.getpixel((i,j)) < threshold):
                bin_img.putpixel((i,j), 0)
            else:
                bin_img.putpixel((i,j), 255)
    return bin_img

                

threshold = getThreshold(grayscale_image, width, height)
bin_img = segment(grayscale_image, threshold, width, height)
bin_img.save('segmented-lord_shen.jpg')