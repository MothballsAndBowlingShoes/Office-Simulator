#
# hallway.rpy
# OfficeSimulator
#
# Created by Atticus Young on 2/21/24.
#
#

default hallwayRooms = ["Boardroom", "Management", "Offices", "Elevator", "Nevermind"]

label hallwayMenu:
    n "What would you like to do?"
    menu:
        "Go farther down the hallway.":
            call neverEndingHallway
        
        "Use the vending machine.":
            call vallory
        
        "Go to the Boss's Office":
            call bossDoor
            
        "Go to Jack's Office":
            call jackOffice
            
        "Go somewhere else.":
            call screen nav_menu(hallwayRooms)
    return
    
label hallway:
    scene bg hallway
    play music backroomsAmbience
    call hallwayMenu

#
# bossDoor
# OfficeSimulator
#
# Created by Atticus Young on 8/2/24.
#
#

label bossDoor:
    scene bg bossdoor with dissolve
    pause 1
    scene bg bossdoor with dissolve:
        zoom 2.0
        xanchor 0.25
        yanchor 0.25
        
    play audio doorJiggle
    pause 1
    n "You try to open the door but it doesn't budge"

label bossDoorOptions:
    menu:
        "Try again":
            play audio doorJiggle
            pause 1
            n "You try to open the door again but it doesn't budge"
            jump bossDoorOptions
            
        "Go back.":
            jump hallway
    return
