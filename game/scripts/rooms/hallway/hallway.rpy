#
# hallway.rpy
# OfficeSimulator
#
# Created by Atticus Young on 2/21/24.
#
#

default hallwayRooms = ["Boardroom", "Management", "Offices", "Elevator", "Nevermind"]
    
label hallwayMenu:
    y "What should I do?"
    menu:   
        "Go farther down the hallway.":
            jump never_ending_hallway_event_manager
            
        "Use the vending machine.":
            jump hallwayVendingMachine
        
        "Go somewhere else.":
            call screen nav_menu(hallwayRooms)

label hallway:
    scene hallway
    play music "music/hallway_ambience.mp3"
    jump hallwayMenu

#
# hallwayVendingMachine
# OfficeSimulator
#
# Created by Atticus Young on 2/21/24.
#
#

# MARK: hallwayVendingMachine entry point
label hallwayVendingMachine:
    
    # Fade to black before showing vending machine image
    show darken with dissolve
    show vending_machine
    
    play music "music/vendingMachineTheme.mp3"
    
    "You approach the Vending Machine."
    "Its LED screen flickers to life with a hypnotic whirr."

    v "Mmmmmm, hey there big boy you here to push my {i}buttons{/i}?~"
    v "Or maybe... You'd like something a bit... saucier?"

label hallwayVendingMachineMenu:
    menu:
        v "Or maybe... You'd like something a bit... saucier?"

        # Option: Buy something
        "Buy something from this mistake of humanity's hubris":
                v "What would you like handsome?"
                jump vendingMachineShops
        
        "Leave while your rectum is still unpenetrated by this steel rectangular prism.":
            jump hallway

return
