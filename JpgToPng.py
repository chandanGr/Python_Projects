from PIL import Image
import sys



def JpgToPng():
    for arg in sys.argv[1:]:
        a, _ = arg.split(".")
        a += ".png"
        img = Image.open(arg)
        img.save(a, "PNG")

JpgToPng()