#
# boardroom.rpy
# OfficeSimulator
#
# Created by Atticus Young on 2/21/24.
#
#
################################################################################
## Variables
################################################################################
default boardroomRooms = ["Hallway", "Nevermind"]

################################################################################
## Labels
################################################################################
## boardroom ###################################################################
#
#
label boardroom:
    scene bg boardroom
    n "You enter the Boardroom"
    n "There's a few employees milling about pretending to be busy"

menu:
    n "What would you like to do?"
    
    "Go somewhere else":
        call screen nav_menu(boardroomRooms)
        
