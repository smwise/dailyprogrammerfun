import os, sys
from PIL import Image, ImageOps


def estimatePi(input_image):
    '''
    Works for single image right now
    Uses only Image
    '''

    pixel_data = input_image.load()
    total_area = 0
    diameter_start = input_image.size[0]
    diameter_stop = 0
    for x in range(input_image.size[0]):
        for y in range(input_image.size[1]):
            if pixel_data[x,y] == (0,0,0):
                total_area += 1
                if x < diameter_start: diameter_start = x
                if x > diameter_stop: diameter_stop = x
    radius = (diameter_stop - diameter_start + 1) / 2
    pi = total_area / (radius * radius)
    return pi


def estimatePiFancier(input_image):
    '''
    Works for single image right now
    Uses other pieces of PIL
    '''

    pixel_data = input_image.load()

    inverted_image = ImageOps.invert(input_image.convert("L"))

    x1, y1, x2, y2 = inverted_image.getbbox()

    total_area = 0
    for x in range(x1, x2):
        for y in range(y1, y2):
            if pixel_data[x,y] == (0,0,0):
                total_area += 1

    radius = (y2-y1) / 2
    pi = total_area / (radius * radius)
    return pi

print("pi for input1 is roughly ", estimatePi(Image.open("input1.png")))
print("pi for input2 is roughly ", estimatePi(Image.open("input2.png")))
