# Built with python 3, dependencies installed with pip 
# library to generate images - Pillow 
# https://pillow.readthedocs.io/en/stable/installation.html
from functools import update_wrapper
from PIL import Image

# library to work with arrays 
# https://numpy.org/
import numpy as np

# library to interact with the operating system
import os

# library to generate random integer values
from random import seed
from random import randint

from numpy.lib.shape_base import dstack

# library to deepcopy
import copy

# custom modules
import lib.coordinates as coordinates
from lib.randomizer import randomize_by_pixel
from lib.rabbit_construction import create_rabbit

# gets path to be used in image creation mechanism, using os
#
# original code, doesn't work
# dirname = os.path.dirname(__file__) 

dirname = os.path.dirname(os.path.abspath(__file__))

# sets final image dimensions as 480x480 pixels
# the original 24x24 pixel image will be expanded to these dimensions
dimensions = 480, 480


# tells how many times to iterate through the following mechanism
# which equals the number of birds
# e.g. 
# for x in range(0-200) 
# would generate 201 birds numbered 0-200

# dictionary to track attributes of each rabbit
rabbit_attr = {}

# dictionary to track how many times each attribute appeared
total_attr = {
    "bg_solid": 0,
    "bg_pixel": 0,
    "sk_solid": 0,
    "sk_pixel": 0,
    "cig": 0,
    "goggle": 0,
    "whisker": 0,
    "candy": 0,
    "robot_arm": 0,
    "jetpack": 0,
    "angel": 0,
    "weed": 0,
    "diamond": 0
}



for x in range(0, 100):

    # using ETH block number as starting random number seed

    #b=13122130
    #seed(x+b)

    # background color
    # randomize bg color
    r, g, b = randint(133, 255), randint(133, 255), randint(133, 255)
    bg = (r, g, b)

    # outline color
    ol = (19, 0, 0)

    # special attributes R colors
    # r1, r2, r3 = (0,0,0), (0,0,0), (0,0,0)

    # randomize skin color
    r, g, b = randint(0, 255), randint(0, 255), randint(0, 255)
    sk = (r, g, b)
    
    # create_rabbit module creates a basic rabbit canvas for us
    basic_rabbit = create_rabbit(bg, ol, sk)

    # Creates a deep copy of the canvas in order to add accessories 
    pixels = copy.deepcopy(basic_rabbit)

    # 1. check for pixelized skin or background
    # 
    # background: 35.00%
    # body: 13.33%

    
    if randint(0, 10000)<= 3500:
        #randomizer for skin by pixel
        randomize_by_pixel(pixels, sk)
    elif randint(0, 10000) <= 1333:
        #randomizer for bg by pixel
        randomize_by_pixel(pixels, bg)


    # 2. check for mouth accessories
    # Total: 45.00%
    # weed: 33.33% * 45.00%
    # cig: 15.00% * 45.00%
    # candy: 51.67% * 45.00%

    mouth_prob = 5500
    if randint(0, 10000) > mouth_prob:
        mouth_attr = True
    try:
        if mouth_attr:
            mouth_accessory = randint(0, 10000)
            print(mouth_accessory)
            if mouth_accessory <= 3333:
                # draw weed
                coordinates.weed_draw(pixels)
                mouth_attr = False
            elif mouth_accessory >= 8500:
                # draw candy
                coordinates.cig_draw(pixels)
                mouth_attr = False
            else:
                coordinates.candy_draw(pixels)
                mouth_attr = False
    except:
        print("No mouth accessory")

    # 3. check for robot arm
    # 
    # Robot Arm: 12.88%
    #

    # Requires special interaction with the back acccessories:
    # Will render robot arm after the back accessories check

    robot_arm_prob = 1288

    if randint(0, 10000) <= robot_arm_prob:
        # Variable to track whehter model has robot arm
        robot_arm_attr = True

        # Variable to track whether the robot arm has been drawn
        robot_drawn = False



    # 4. check for jetback or angel
    # Totaly: 18.88%
    # Angel_Wing: 76.67% * 18.88%
    # Jet_Pack: 23.33% 18.88%

    back_prob = 1888

    jetpack_prob = 2333

    if randint(0, 10000) <= back_prob:
        back_attr = True
    try:
        if back_attr:
            # Check which back item will be drawn
            # Need special logic for interaction with the robot arm accessory
            back_accessory = randint(0, 10000)
            if back_accessory <= jetpack_prob and robot_arm_attr:
                coordinates.robot_arm_draw(pixels)
                coordinates.jetpack_draw(pixels)
                # set back attributes back to false after it's drawn
                back_attr = False

                # set robot arm attribute back to false after it's drawn
                robot_arm_attr = False

                # robot has been drawn
                robot_drawn = True

            elif back_accessory > jetpack_prob and robot_arm_attr: 
                coordinates.angel_draw(pixels)
                coordinates.robot_arm_draw(pixels)
                back_attr = False
                robot_arm_attr = False
                robot_drawn = True

            elif back_accessory <= jetpack_prob:
                coordinates.jetpack_draw(pixels)
                back_attr = False
            
            elif back_accessory > jetpack_prob:
                coordinates.angel_draw(pixels)
                back_attr = False
    
    except:
        print("No back accessory")

    
    try:
        # check whether the robot arm has been drawn
        if robot_arm_attr and not robot_drawn:
            coordinates.robot_arm_draw(pixels)
            # set arm attribute back after it's drawn
            robot_arm_attr = False

            # reset arm drawn tracker after it's drawn
            robot_drawn = False
    
    except: 
        print("No robot arm accessory")



    # 5. check for whisker
    # 
    # Whisker: 5.88%
    #
    whisker_prob = 588
    
    if randint(0, 10000) < whisker_prob:
        whisker_attr = True
    try:
        if whisker_attr:
            coordinates.whisker_draw(pixels)
            whisker_attr = False
    except:
        print("Not a wise rabbit")




    # 6. check for diamond
    # 
    # Diamond: 2.88%
    #

    diamond_prob = 288
    
    if randint(0, 10000) <= diamond_prob:
        diamond_attr = True
    try:
        if diamond_attr:
            coordinates.whisker_draw(pixels)
            diamond_attr = False
    except:
        print("Paper Hand")
    
    # 7. check for goggle
    #
    # Goggle: 31.37
    #

    goggle_prob = 3137
    
    if randint(0, 10000) <= goggle_prob:
        goggle_attr = True
    try:
        if goggle_attr:
            coordinates.whisker_draw(pixels)
            goggle_attr = False
    except:
        print("Does not have a goggle")
 

    # convert the pixels into an array using numpy
    array = np.array(pixels, dtype=np.uint8)

    # use PIL to create an image from the new array of pixels
    new_image = Image.fromarray(array)
    new_image = new_image.resize(dimensions, resample=0)
    imgname = dirname + '/rabbit_images/' + (str(x)) + '.png'
    new_image.save(imgname)





