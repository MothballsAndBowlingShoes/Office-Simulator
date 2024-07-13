#
# hallway.rpy
# OfficeSimulator
#
# Created by Atticus Young on 2/21/24.
#
#

label hallway:
    scene hallway
    play music "music/hallway_ambience.mp3"
    
    

label hallway_menu:
    y "What should I do?"
    
    menu:
        y "What should I do?"
        "Management's office":
            jump management
            
        "Go farther down the hallway.":
            jump never_ending_hallway_event_manager
            
        "Use the vending machine.":
            jump hallway_vendingMachine
        
        "Go somewhere else.":
            jump hallway_navigation
            
    return

#
# hallway_vendingMachine
# OfficeSimulator
#
# Created by Atticus Young on 2/21/24.
#
#

# MARK: hallway_vendingMachine entry point
label hallway_vendingMachine:
    
    # Fade to black before showing vending machine image
    show darken with dissolve
    show vending_machine
    
    play music "music/vendingMachineTheme.mp3"
    
    "You approach the Vending Machine."
    "Its LED screen flickers to life with a hypnotic whirr."

    v "Mmmmmm, hey there big boy you here to push my {i}buttons{/i}?~"
    v "Or maybe... You'd like something a bit... saucier?"

label hallway_vendingMachine_Menu:
    menu:
        v "Or maybe... You'd like something a bit... saucier?"

        # Option: Buy something
        "Buy something from this mistake of humanity's hubris":
                v "What would you like handsome?"
                jump vendingMachineShops
        
        "Leave while your rectum is still unpenetrated by this steel rectangular prism.":
            jump hallway

return

#
# hallway_navigation
# OfficeSimulator
#
# Created by Atticus Young on 2/21/24.
#
#

label hallway_navigation:
    "Where should I go?"
    menu:
        "Where should I go?"
        
        "Boardroom":
            jump boardroom
            
        "Management":
            jump management
            
        "Offices":
            jump offices
            
        "Elevator":
            jump elevator
            
        "Nevermind":
            jump hallway_menu

return
