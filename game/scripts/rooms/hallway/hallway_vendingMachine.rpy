# 
# hallway_vendingMachine.rpy
# OfficeSimulator
#
# Created by Atticus Young on 2/21/24.
# 
# 

# MARK: hallway_vendingMachine entry point
label hallway_vendingMachine:
    n "You approach the Vending Machine."
    n "It's LED screen flickers too life with a hypnotic whirr"
    show darken with dissolve
    show vending_machine
    v "Mmmmmm, hey there big boy you here to push my {i}buttons{/i}?~"
    v "Or maybe... You'd like something a bit... saucier?"
    menu:
        v "Or maybe... You'd like something a bit... saucier?"
        
        "Buy something from this mistake of humanty's hubris":
                jump vending_machine_shop
    return
