total_attr = {
    "bg_solid": 0, x
    "bg_pixel": 0, x
    "sk_solid": 0, x
    "sk_pixel": 0, x
    "cig": 0, x
    "goggle": 0,
    "whisker": 0,
    "candy": 0, x
    "robot_arm": 0,
    "jetpack": 0,
    "angel": 0,
    "weed": 0, x
    "diamond": 0
}

if x < 5:
  print("a")
elif 


for x in range(0, n):
    # initialize attribute tracker for each rabbits
    # tracking background color, skin color, and total accessories
    rabbit_attr[n] = {
        "bg_rgb": "",
        "bg_color": "",
        "sk_rgb": "",
        "sk_color": "",
        "acc": []
    }
    rabbit_attr[n]["bg_rgb"] = n


def closest_colour(requested_colour):
    min_colours = {}
    for key, name in webcolors.CSS3_HEX_TO_NAMES.items():
        r_c, g_c, b_c = webcolors.hex_to_rgb(key)
        rd = (r_c - requested_colour[0]) ** 2
        gd = (g_c - requested_colour[1]) ** 2
        bd = (b_c - requested_colour[2]) ** 2
        min_colours[(rd + gd + bd)] = name
    return min_colours[min(min_colours.keys())]

def get_colour_name(requested_colour):
    try:
        closest_name = actual_name = webcolors.rgb_to_name(requested_colour)
    except ValueError:
        closest_name = closest_colour(requested_colour)
        actual_name = None
    return actual_name, closest_name

requested_colour = (119, 172, 152)
actual_name, closest_name = get_colour_name(requested_colour)