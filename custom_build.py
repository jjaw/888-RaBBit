# this file allow you to generate accesory of your choice
# Used to draw anything you want

import lib.coordinates as coordinates
from lib.rabbit_construction import create_rabbit
import copy
import os
from random import randint
from random import seed
from lib.randomizer import randomize_by_pixel
from PIL import Image
import numpy as np

dirname = os.path.dirname(os.path.abspath(__file__))

dimensions = 480, 480

# background color
# randomize bg color

bg = (72, 72, 72)

# outline color
ol = (19, 0, 0)

# special attributes R colors
# r1, r2, r3 = (0,0,0), (0,0,0), (0,0,0)

# randomize skin color
sk = (233, 233, 233)

# using the create_rabbit module to construct a new rabbit
basic_rabbit = create_rabbit(bg, ol, sk)

def special_draw(base):
    funcs = [coordinates.cig_draw, coordinates.goggle_draw,
         coordinates.whisker_draw, coordinates.candy_draw,
         coordinates.robot_arm_draw, coordinates.jetpack_draw,
         coordinates.angel_draw, coordinates.weed_draw,
         coordinates.diamond_draw
         ]
    names = ["cig", "goggle", "whisker", "candy", "robot_arm", "jetpack", "angel", "weed", "diamond"]


    for i, func in enumerate(funcs):

        pixels = copy.deepcopy(base)
        # randomize bg color
        # bg_x, bg_y, bg_z = randint(88, 255), randint(88, 255), randint(88, 255)
        # bg = (bg_x, bg_y, bg_z)
        
        """ uncomment this part if you wish to pixeliate bg or sk
        # seed(1+i)
        # if randint(0, 50)< 25:
        
        # randomizer for skin by pixel
        #    randomize_by_pixel(pixels, sk)
        # else:
        #    randomize_by_pixel(pixels, bg)
        """

        func(pixels)
        array = np.array(pixels, dtype=np.uint8)
        
        # use PIL to create an image from the new array of pixels
        new_image = Image.fromarray(array)
        new_image = new_image.resize(dimensions, resample=0)
        imgname = dirname + '/custom_rabbit_images/' + names[i] + '.png'
        new_image.save(imgname)
        pixels = []

special_draw(basic_rabbit)
