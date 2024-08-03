# 
# vallory.rpy
# Office-Simulator
#
# Created by Atticus Young on 8/2/24.
# 
# 

# MARK: vallory entry point
label vallory:
    # Fade to black before showing vending machine image
    show darken with dissolve
    show vallory neutral
    
    play music valloryTheme
    
    n "You approach the Vending Machine."
    n "Its LED screen flickers to life with a hypnotic whirr."
    
    v "Mmmmmm, hey there big boy you here to push my {i}buttons{/i}?~"
    v "Or maybe... You'd like something a bit... saucier?"

label valloryMenu:
    menu:
        v "Or maybe... You'd like something a bit... saucier?"
        
        # Option: Buy something
        "Buy something from this mistake of humanity's hubris":
            v "What would you like handsome?"
            call hallway_vendingMachineMenu_vendingMachineShops
        
        "Leave while your rectum is still unpenetrated by this steel rectangular prism.":
            jump hallway
            
    return
