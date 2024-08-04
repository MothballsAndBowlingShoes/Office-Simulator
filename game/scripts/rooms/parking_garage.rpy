#
# parkingGarage.rpy
# OfficeSimulator
#
# Created by Atticus Young on 8/2/24.
#
#

########################################################################################
## Variables
########################################################################################
default garageRooms = ["Elevator", "Nevermind"]

########################################################################################
## Labels
########################################################################################
## parkingGarage #######################################################################
##
## This code defines the parking garage label.
label parkingGarage:
    scene bg garage
    n "You enter the Parking Garage"
    n "it smells of Motor oil and Dead Skunk"
    menu:
        n "What would you like to do?"
        
        "Go Somewhere else":
            call screen nav_menu(garageRooms)
