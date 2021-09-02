# Built with python 3, dependencies installed with pip 
# library to generate images - Pillow 
# https://pillow.readthedocs.io/en/stable/installation.html
from PIL import Image

import csv

# library to convert rgb code to name
from webcolors import rgb_to_name
import webcolors

# library to work with arrays 
# https://numpy.org/
import numpy as np
import pandas as pd

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
import lib.trackers

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

tracker = {}

def render_random_image(seed, n):
    # dictionary to track attributes of each rabbit   
    rabbit_attr = {}

    # dictionary to track how many times each attribute appeared
    total_attr = lib.trackers.total_attr


    for x in range(0, n):
        # initialize attribute tracker for each rabbits
        # tracking background color, skin color, and total accessories
        rabbit_attr[x] = {
            "bg_rgb": "",
            "bg_color": "",
            "sk_rgb": "",
            "sk_color": "",
            "acc": []
        }

        # background color
        # randomize bg color
        r, g, b = randint(133, 255), randint(133, 255), randint(133, 255)
        bg = (r, g, b)
        rabbit_attr[x]["bg_rgb"] = bg
        
        try:
            rabbit_attr[x]["bg_color"] = rgb_to_name(bg, spec='css3')
        except:
            rabbit_attr[x]["bg_color"] = "None"
            
        # outline color
        ol = (19, 0, 0)

        # special attributes R colors
        # r1, r2, r3 = (0,0,0), (0,0,0), (0,0,0)

        # randomize skin color
        r, g, b = randint(0, 255), randint(0, 255), randint(0, 255)
        sk = (r, g, b)
        rabbit_attr[x]["sk_rgb"] = sk
        try:
            rabbit_attr[x]["sk_color"] = rgb_to_name(sk, spec='css3')
        except:
            rabbit_attr[x]["sk_color"] = "None"
        
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
            rabbit_attr[x]["sk_color"] = "pixelated"
            # counter to track attribute count of the total collection
            total_attr["sk_pixel"] += 1

        else:
            total_attr["sk_solid"] += 1


        if randint(0, 10000) <= 1333:
            #randomizer for bg by pixel
            randomize_by_pixel(pixels, bg)
            rabbit_attr[x]["bg_color"] = "pixelated"
            total_attr["bg_pixel"] += 1

        else:
            total_attr["bg_solid"] += 1


        # 2. check for mouth accessories
        #
        # Total: 55.55%
        # weed: 33.33% * 55.55%
        # cig: 15.00% * 55.5%
        # candy: 51.67% * 55.55%

        mouth_prob = 5555
        mouth_attr = False

        if randint(0, 10000) <= mouth_prob:
            mouth_attr = True
        
        if mouth_attr:
            mouth_accessory = randint(0, 10000)

            if mouth_accessory <= 3333:
                # draw weed
                coordinates.weed_draw(pixels)
                rabbit_attr[x]["acc"].append("weed")
                total_attr["weed"] += 1
                mouth_attr = False
            elif mouth_accessory >= 8500:
                # draw cig
                burn_color = coordinates.cig_draw(pixels)
                rabbit_attr[x]["acc"].append("cig"+ burn_color)

                # tracking cig by burn color
                if burn_color == "_red_burn":
                    total_attr["cig_red"] += 1
                else:
                    total_attr["cig_blue"] +=1 
                mouth_attr = False
            else:
                # draw candy
                candy_color = coordinates.candy_draw(pixels)
                rabbit_attr[x]["acc"].append("candy" + candy_color)

                # tracking cig by burn color
                if candy_color == "_red":
                    total_attr["candy_red"] += 1
                else:
                    total_attr["candy_green"] +=1 
                
                mouth_attr = False
        else:
            print("No mouth accessory")

        # 3. check for robot arm
        # 
        # Robot Arm: 15.88%

        # Requires special interaction with the back acccessories:
        # Will render robot arm after the back accessories check

        robot_arm_prob = 1588

        robot_arm_attr = False

        # robot_drawn starts as TRUE, shows that it has already been drawn.
        # only when robot_drawn == False and robot_arm_attr == True will the robot_arm be drawn
        robot_drawn = True

        if randint(0, 10000) <= robot_arm_prob:
            # Variable to track whehter model has robot arm
            robot_arm_attr = True

            # Variable to track whether the robot arm has been drawn
            robot_drawn = False



        # 4. check for jetback or angel
        # Totaly: 18.88%
        # Angel_Wing: 76.67% * 18.88%
        # Jet_Pack: 23.33% * 18.88%

        back_prob = 1888
        jetpack_prob = 2333
        back_attr = False

        if randint(0, 10000) <= back_prob:
            back_attr = True
        
        if back_attr:
            # Check which back item will be drawn
            # Need special logic for interaction with the robot arm accessory
            back_accessory = randint(0, 10000)
            if back_accessory <= jetpack_prob and robot_arm_attr:
                coordinates.robot_arm_draw(pixels)
                coordinates.jetpack_draw(pixels)
                rabbit_attr[x]["acc"].append("robot_arm")
                rabbit_attr[x]["acc"].append("jetpack")
                total_attr["robot_arm"] += 1
                total_attr["jetpack"] += 1
                # set back attributes back to false after it's drawn
                back_attr = False

                # set robot arm attribute back to false after it's drawn
                robot_arm_attr = False

                # robot has been drawn
                robot_drawn = True

            elif back_accessory > jetpack_prob and robot_arm_attr: 
                coordinates.angel_draw(pixels)
                coordinates.robot_arm_draw(pixels)
                rabbit_attr[x]["acc"].append("angel")
                rabbit_attr[x]["acc"].append("robot_arm")
                total_attr["angel"] += 1
                total_attr["robot_arm"] += 1
                back_attr = False
                robot_arm_attr = False
                robot_drawn = True

            elif back_accessory <= jetpack_prob:
                coordinates.jetpack_draw(pixels)
                rabbit_attr[x]["acc"].append("jetpack")
                total_attr["jetpack"] += 1
                back_attr = False
            
            elif back_accessory > jetpack_prob:
                coordinates.angel_draw(pixels)
                rabbit_attr[x]["acc"].append("angel")
                total_attr["angel"] += 1
                back_attr = False
        
        else:
            print("No back accessory")

        
        
        # check whether the robot arm has been drawn
        if robot_arm_attr and not robot_drawn:
            coordinates.robot_arm_draw(pixels)
            rabbit_attr[x]["acc"].append("robot_arm")
            total_attr["robot_arm"] += 1
            # set arm attribute back after it's drawn
            robot_arm_attr = False

            # reset arm drawn tracker after it's drawn
            robot_drawn = False
    
        else:
            print("No robot arm accessory")



        # 5. check for whisker
        # 
        # Whisker: 8.88%
        #
        whisker_prob = 888
        whisker_attr = False
        
        if randint(0, 10000) < whisker_prob:
            whisker_attr = True
        
        if whisker_attr:
            coordinates.whisker_draw(pixels)
            rabbit_attr[x]["acc"].append("whisker")
            total_attr["whisker"] += 1
            whisker_attr = False
        else:
            print("Not a wise rabbit")

        # 6. check for goggle
        #
        # Goggle: 31.37
        #

        goggle_prob = 3137
        goggle_attr = False
        
        if randint(0, 10000) <= goggle_prob:
            goggle_attr = True
        
        if goggle_attr:
            lens_color = coordinates.goggle_draw(pixels)

            # tracking goggle by lens color
            if lens_color == "_cyan_lens":
                total_attr["goggle_cyan"] += 1
            elif lens_color == "_yellow_lens":
                total_attr["goggle_yellow"] += 1
            elif lens_color == "_magenta_lens":
                total_attr["goggle_magenta"] += 1 
            else:
                total_attr["goggle_white"] += 1

            rabbit_attr[x]["acc"].append("goggle" + lens_color)

            goggle_attr = False
        else:
            print("Does not have a goggle")
            

        # 7. check for diamond
        # 
        # Diamond: 2.88%
        #

        diamond_prob = 288
        diamond_attr = False

        if randint(0, 10000) <= diamond_prob:
            diamond_attr = True
        
        if diamond_attr:
            coordinates.diamond_draw(pixels)
            rabbit_attr[x]["acc"].append("diamond")
            total_attr["diamond"] += 1
            diamond_attr = False
        else:
            print("Paper Hand")
            
        


        # sort rabbit personal attributes
        rabbit_attr[x]["acc"].sort
    
        print("Assembling... number " + str(x))

        # convert the pixels into an array using numpy
        array = np.array(pixels, dtype=np.uint8)

        # use PIL to create an image from the new array of pixels
        new_image = Image.fromarray(array)
        new_image = new_image.resize(dimensions, resample=0)
        imgname = dirname + '/rabbit_images/' + (str(x)) + '.png'
        new_image.save(imgname)
        

    # dump total stats
    (pd.DataFrame.from_dict(data=total_attr, orient='index')
        .to_csv('total_stats.csv', mode="w"))

    # dump rabbit individual stat
    (pd.DataFrame.from_dict(data=rabbit_attr, orient='index')
        .to_csv('rabbit_stats.csv', mode="w"))

# render_random_image(int seed_x, int num)
# seed: for random.seed()
# num: number of images to generate
seed_num = 13145929 # ETH at the time of generation
num = 500
render_random_image(seed_num, num)