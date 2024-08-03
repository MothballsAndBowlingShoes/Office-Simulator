
default boardroomRooms = ["Hallway", "Nevermind"]

label boardroom:
    scene bg boardroom
    n "You enter the Boardroom"
    n "There's a few employees milling about pretending to be busy"


label boardroomMenu:
    menu:
        n "What would you like to do?"
        
        "Go somewhere else":
            call screen nav_menu(boardroomRooms)
        
