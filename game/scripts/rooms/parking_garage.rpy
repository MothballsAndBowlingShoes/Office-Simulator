#
# parkingGarage.rpy
# OfficeSimulator
#
# Created by Atticus Young on 8/2/24.
#
#

default garageRooms = ["Elevator", "Nevermind"]
label parkingGarage:
    scene bg garage
    n "You enter the Parking Garage"
    n "it smells of Motor oil and Dead Skunk"

label parkingGarageMenu:
    menu:
        n "What would you like to do?"
        
        "Go Somewhere else":
            call screen nav_menu(garageRooms)
