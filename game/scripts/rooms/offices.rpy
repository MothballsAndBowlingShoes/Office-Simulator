#
# offices.rpy
# Office-Simulator
#
# Created by Atticus Young on 8/1/24.
#
#
########################################################################################
## Labels
########################################################################################
## offices #############################################################################
label offices:
    scene bg offices
    n "You enter the Offices"
    
    menu:
        "Go to your cubicle":
            jump cubicle
        "Go to Randy's Cubicle":
            jump randy
        "Go back":
            jump hallway
