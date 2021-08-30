from random import randint

def randomize_by_pixel(canvas, attr):
# This will randomize color of the selected attribute by pixel
    x, y = 188, 255
    for q, pixels in enumerate(canvas):
        for p, pixel in enumerate(pixels):
            if pixel == attr:
                pixel_color = (randint(x, y), randint(x, y), randint(x, y))
                canvas[q][p] = pixel_color