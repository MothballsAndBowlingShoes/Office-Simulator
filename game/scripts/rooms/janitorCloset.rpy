#
# janitorCloset.rpy
# OfficeSimulator
#
# Created by Atticus Young on 2/21/24.
#
#
################################################################################
## Variables
################################################################################
default ratGrabbed = False
default firstTimeInRoom = False

image deadRatInHand = "images/hand_deadRat.png"

################################################################################
## Labels
################################################################################
## label_janitorCloset #####################################################################
##
## This code defines a label named 'janitorCloset' and sets the scene background to 'janitorcloset'.
## The character enters the closet, which is described as smelling of mold and cigarette smoke.
## A dead rat in the corner is also mentioned. Depending on whether or not the player has
## grabbed the rat before entering this room and if it's their first time in the room,
## different dialogues are displayed to inform about the presence of the dead rat.
##
## The code then presents a menu with one option, "Grab rat", but only if the rat hasn't been
## grabbed yet and it's the player's first time in the room. Upon selecting this option,
## the game shows an image of the dead rat at the left side of the screen and displays another
## dialogue asking why the player wants to pick up a dead rat.
##
## If the player chooses to continue with picking up the dead rat, it prompts another menu
## to choose from. The first choice in this nested menu would add the dead rat to the inventory
## and remove its image from the screen while setting 'ratGrabbed' variable to True. Selecting any
## other options will not change the 'ratGrabbed' variable but only display additional dialogues.
##
## If the player decides against picking up the dead rat, they can choose to go back by selecting
## the "Go Back" option which then jumps back to the 'lobby' label.
label janitorCloset:
    scene bg janitorcloset
    
    n "You enter the janitor's closet."
    n "It smells of mold and cigarette smoke."
    
    if ratGrabbed == False and firstTimeInRoom == False:
        n "There's even a dead rat in the corner!"
        $ firstTimeInRoom = True
    elif ratGrabbed == False:
        n "The dead rat is still there!"
    
    if metGiuseppe == False:
        call giuseppe
    
    menu:
        "Grab rat" if ratGrabbed == False:
            show deadRatInHand at left
            n "Why would you pick up a dead rat?!?"
            
            menu:
                "PICK UP THE DEAD RAT.":
                    n "WHY DO YOU WANT THE DEAD RAT?"
                    menu:
                        "PICK UP RAT.":
                            menu:
                                "THE PEOPLE SHALL KNOW PLAGUE.":
                                    menu:
                                        "NO ONE IS SAFE FROM MY DEAD RAT.":
                                            n "..."
                                            menu:
                                                "...":
                                                    n "{i}You pick up the dead rat...{/i}"
                                                    $ inventory.append(deadRat)
                                                    $ ratGrabbed = True
                                                    hide deadRatInHand
                                                    jump janitorCloset
        
        "Go Back":
            jump lobby
