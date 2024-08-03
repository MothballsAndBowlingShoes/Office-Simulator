# 
# cubicle.rpy
# Office-Simulator
#
# Created by Atticus Young on 8/2/24.
# 
# 

default firstVisit = True

# MARK: cubicle entry point
label cubicle:
    scene bg cubicle
    if firstVisit:
        n "This is your cubicle."
        menu:
            "Wow!":
                n "This is where you can do all your work for the office, or screw around and look at cat pics and women on the internet"
                menu:
                    "WOW!":
                        n "Now get to work ya scamp!"
                        $ firstVisit = False
                        with fade
    jump cubicleMenu

label cubicleMenu:
    menu:
        "What would you like to do?"
        
        "Use the computer":
            "Call Computer Screen"
            jump cubicleMenu
        "Go back":
            jump offices
    return
