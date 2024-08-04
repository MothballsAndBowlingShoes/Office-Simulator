# 
# cubicle.rpy
# Office-Simulator
#
# Created by Atticus Young on 8/2/24.
# 
#

########################################################################################
## Variables
########################################################################################
default firstVisit = True

########################################################################################
## Labels
########################################################################################
## label_cubicle #######################################################################
##
## This code defines a label named 'cubicle' and sets the scene background to 'cubicle'.
## If it's the first visit, it displays a dialogue box saying "This is your cubicle." with
## a menu option for the character to respond "Wow!". Upon selecting this response,
## another dialogue box appears showing a description of what the cubicle can be used for.
## The code also includes a submenu with options to either "WOW!" or choose an alternative
## option. Once the player selects an option, it sets 'firstVisit' variable to False and uses
## the 'fade' transition effect before jumping back to the 'cubicleMenu'.
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
    
## cubicleMenu #########################################################################
##
## This code defines a label named 'cubicleMenu'. It displays a menu with the title "What would you like to do?".
## The menu has two options: "Use the computer" and "Go back". Choosing the "Use the computer"
## option triggers another function called "Call_Computer_Screen", whereas selecting "Go back"
## jumps back to the 'offices' label. Finally, the code includes a return statement to return
## to the previous function or state before this menu was displayed.
label cubicleMenu:
    menu:
        "What would you like to do?"
        
        "Use the computer":
            # MARK: Implement Computer Menu
            jump cubicleMenu
        "Go back":
            jump offices
    return
