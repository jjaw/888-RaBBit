#interactions

# jet pack OR angel # WARNING:
# cig or


# robot and jetpack,
# paint robot first, then jetpack

# robot and angel
# paint angel first then robot

# robot and whiskter
# paint robot first then whiskter

#always paint diamond last

#special coordinates

r1 = [20, 24]
r2 = [20, 5], [21, 5]
r3 = [4, 23], [5, 23], [6, 23]
r4 = [5, 23]

# cig
# goggle
# whisker
# candy
# robot arm
# jetpack
# angel
# weed
# diamond


border_color = (19, 0, 0)


#1. cig

def cig_draw(base):
       #brownish
       cig_butt_rbg = (121, 85, 0)

       #whiteish
       cig_stick_rbg = (231, 231, 231)

       #reddish
       cig_burn_rbg = (255, 60, 0)

       #greyishi
       cig_smoke_rbg = (207, 207, 207)


       cig_butt_xy = [7, 12]
       cig_stick_xy = [5, 12], [6, 12]
       cig_burn_xy = [4, 12]
       cig_smoke_xy = [3, 11], [2, 10]

       for x in cig_stick_xy:
              q, p = x[1], x[0]

              base[q][p] = cig_stick_rbg

       for x in cig_smoke_xy:
              q, p = x[1], x[0]

              base[q][p] = cig_smoke_rbg

       q, p = cig_burn_xy[1], cig_burn_xy[0]
       base[q][p] = cig_burn_rbg

       q, p = cig_butt_xy[1], cig_butt_xy[0]
       base[q][p] = cig_butt_rbg

#2. goggle

def goggle_draw(base):
       goggle_border_rbg = (19, 0, 0)
       goggle_lens_rbg = (0, 255, 246)


       goggle_border_xy = [
              [14, 5],
              [15, 6],
              [9, 7],
              [8, 8], [9, 8], [10, 8], [11, 8],
              [8, 9], [11, 9], [12, 9], [13, 9], [14, 9],
              [8, 10], [9, 10], [10, 10], [11, 10], [15, 9]
       ]

       goggle_lens_xy = [[9, 9], [10, 9]]

       for x in goggle_border_xy:
              q, p = x[1], x[0]

              base[q][p] = goggle_border_rbg

       for x in goggle_lens_xy:
              q, p = x[1], x[0]

              base[q][p] = goggle_lens_rbg



#3. whisker

def whisker_draw(base):
       whisker_rbg = (184, 184, 184)

       whisker_xy = [
              [7, 12],
              [6, 13], [8, 13],
              [6, 14], [8, 14],
              [6, 15], [8, 15],
              [8, 16]
       ]

       for x in whisker_xy:
              q, p = x[1], x[0]

              base[q][p] = whisker_rbg



#4. candy

def candy_draw(base):
       candy_white_rbg = (245, 245, 245)
       candy_red_rbg = (245, 0, 0)

       candy_white_xy = [
              [3, 11],
              [5, 12], [7, 12]
       ]

       candy_red_xy = [
       [4, 10],
       [4, 12], [6, 12]
       ]

       for x in candy_white_xy:
              q, p = x[1], x[0]

              base[q][p] = candy_white_rbg

       for x in candy_red_xy:
              q, p = x[1], x[0]

              base[q][p] = candy_red_rbg

#5. robot arm

def robot_arm_draw(base):
       robot_arm_border_rbg = (19, 0, 0)
       robot_arm_burn_out_rbg = (255, 108, 0)
       robot_arm_burn_cent_rbg = (255, 0, 0)
       robot_arm_metal_rbg = (171, 171, 171)
       robot_arm_high_light_rbg = (84, 49, 197)


       robot_arm_border_xy = [
              [9, 12], [10, 12], [11, 12], [12, 12], [13, 12], [14, 12], [15, 12],
              [9, 13], [16, 13],
              [9, 14], [16, 14],
              [8, 15], [9, 15], [10, 15], [13, 15], [14, 15], [15, 15], [16, 15],
              [8, 16], [13, 16],
              [8, 17], [13, 17],
              [9, 18], [10, 18], [11, 18], [12, 18]
       ]

       robot_arm_burn_out_xy = [
                     [5, 15], [7, 15],
                     [7, 16],
                     [5, 17], [6, 17]
       ]

       robot_arm_burn_cent_xy = [6, 16]

       robot_arm_metal_xy = [
              [10, 13], [11, 13], [14, 13],
              [11, 14], [12, 14], [13, 14], [15, 14],
              [12, 15],
              [9, 16], [10, 16], [12, 16],
              [9, 17], [11, 17], [12, 17]
       ]

       robot_arm_high_light_xy = [
              [12, 13], [13, 13], [15, 13],
              [10, 14], [14, 14],
              [11, 15],
              [11, 16],
              [10, 17]
       ]

       for x in robot_arm_border_xy:
              q, p = x[1], x[0]

              base[q][p] = robot_arm_border_rbg
       
       for x in robot_arm_burn_out_xy:
              q, p = x[1], x[0]

              base[q][p] = robot_arm_burn_out_rbg
       
       for x in robot_arm_metal_xy:
              q, p = x[1], x[0]

              base[q][p] = robot_arm_metal_rbg
       
       for x in robot_arm_high_light_xy:
              q, p = x[1], x[0]

              base[q][p] = robot_arm_high_light_rbg
       
       q, p = robot_arm_burn_cent_xy[1], robot_arm_burn_cent_xy[0]

       base[q][p] = robot_arm_burn_cent_rbg

#6. angel

def angel_draw(base):
       angel_halo_rbg = (255, 156, 0)
       angel_wing_dark_rbg = (175, 175, 175)
       angel_wing_light_rbg = (211, 211, 211)

       angel_halo_xy = [
              [14, 4],
              [9, 5], [15, 5],
              [8, 6], [14, 6],
              [9, 7], [10, 7], [11, 7], [12, 7], [13, 7]
       ]

       angel_wing_dark_xy = [
              [16, 10], [17, 10], [18, 10],
              [15, 11], [19, 11],
              [14, 12], [16, 12], [20, 12],
              [14, 13],
              [13, 14]
       ]

       angel_wing_light_xy = [
              [16, 11], [17, 11], [18, 11],
              [15, 12]
       ]

       for x in angel_halo_xy:
              q, p = x[1], x[0]

              base[q][p] = angel_halo_rbg

       for x in angel_wing_dark_xy:
              q, p = x[1], x[0]

              base[q][p] = angel_wing_dark_rbg
       
       for x in angel_wing_light_xy:
              q, p = x[1], x[0]

              base[q][p] = angel_wing_light_rbg

#7. jetpack,



def jetpack_draw(base):
       jetpack_metal_rbg = (114, 114, 114)
       jetpack_flame_rbg = (255, 0, 0)

       jetpack_metal_xy = [
                     [17, 8], [18, 8],
                     [17, 9], [18, 9],
                     [17, 10], [18, 10],
                     [16, 11], [17, 11], [18, 11],
                     [12, 12], [13, 12], [15, 12], [17, 12], [18, 12],
                     [12, 13], [13, 13], [14, 13],
                     [12, 14], [13, 14],
                     [12, 15], [13, 15],
                     [12, 16], [13, 16]
       ]

       jetpack_flame_xy = [
                     [17, 13], [18, 13],
                     [18, 14],
                     [12, 17], [13, 17],
                     [13, 18]
       ]

       for x in jetpack_metal_xy:
              q, p = x[1], x[0]

              base[q][p] = jetpack_metal_rbg

       for x in jetpack_flame_xy:
              q, p = x[1], x[0]

              base[q][p] = jetpack_flame_rbg

#8. diamond

def diamond_draw(base):
       diamond_border_rbg = (19, 0, 0)
       diamond_shine_rbg = (116, 193, 215)
       diamond_base_rbg = (0, 159, 205)

       diamond_border_xy = [
              [15, 13], [16, 13], [17, 13],
              [14, 14], [18, 14],
              [14, 15], [18, 15],
              [15, 16], [17, 16],
              [16, 17]
       ]

       diamond_shine_xy = [
              [15, 14], [17, 14],
              [16, 15]
       ]

       diamond_base_xy = [
              [16, 14],
              [15, 15], [17, 15],
              [16, 16]
       ]
       for x in diamond_border_xy:
              q, p = x[1], x[0]

              base[q][p] = diamond_border_rbg

       for x in diamond_base_xy:
              q, p = x[1], x[0]

              base[q][p] = diamond_base_rbg

       for x in diamond_shine_xy:
              q, p = x[1], x[0]

              base[q][p] = diamond_shine_rbg



#9. weed

def weed_draw(base):
       #greenish
       weed_body_rbg = (30, 137, 85)

       #reddish
       weed_burn_rbg = (255, 60, 0)

       #greyishi
       weed_smoke_rbg = (207, 207, 207)

       weed_body_xy = [[5, 12], [6, 12], [7, 12]]
       weed_burn_xy = [4, 12]
       weed_smoke_xy = [[3, 11], [2, 10]]

       for x in weed_body_xy:
              q, p = x[1], x[0]

              base[q][p] = weed_body_rbg

       for x in weed_smoke_xy:
              q, p = x[1], x[0]

              base[q][p] = weed_smoke_rbg
       
       q, p = weed_burn_xy[1], weed_burn_xy[0]
       base[q][p] = weed_burn_rbg
