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

## janitorCloset ###############################################################
##
## The main handler for the janitor scene when the player first enters.

label janitorCloset:
    scene bg janitorcloset
    
    n "You enter the janitor's closet."
    n "It smells of mold and cigarette smoke."
    
    if ratGrabbed == False and firstTimeInRoom == False:
        n "There's even a dead rat in the corner!"
        $ firstTimeInRoom = True
    elif ratGrabbed == False:
        n "The dead rat is still there!"
    
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
