import sys
from PIL import Image

try:
    img = Image.open('assets/images/footer-logo-white.png').convert('RGBA')
    pixels = img.load()
    w, h = img.size

    for y in range(345):
        for x in range(560, w):
            r, g, b, a = pixels[x, y]
            if r > 150 and g > 150 and b > 150:
                pixels[x, y] = (234, 38, 41, a)

    img.save('assets/images/footer-logo-red.png')
    print("Saved footer-logo-red.png")
except Exception as e:
    print("Error:", e)
