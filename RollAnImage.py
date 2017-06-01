from PIL import Image
import sys

image = Image.open(sys.argv[1])
number = int(sys.argv[2])

def roll(image, delta):
    xsize, ysize = image.size

    part1 = image.crop((0, 0, delta, ysize))
    part2 = image.crop((delta, 0, xsize, ysize))

    image.paste(part2, (0, 0, xsize-delta, ysize))
    image.paste(part1, (xsize-delta, 0, xsize, ysize))

    return image

a = roll(image, number)
a.show()