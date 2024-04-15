# 
# hallway_vendingMachine.rpy
# OfficeSimulator
#
# Created by Atticus Young on 2/21/24.
# 
# 

# MARK: hallway_vendingMachine entry point
label hallway_vendingMachine:

    "You approach the Vending Machine."
    "Its LED screen flickers to life with a hypnotic whirr."

    # Fade to black before showing vending machine image
    show darken with dissolve
    show vending_machine

    v "Mmmmmm, hey there big boy you here to push my {i}buttons{/i}?~"
    v "Or maybe... You'd like something a bit... saucier?"

    menu:
        v "Or maybe... You'd like something a bit... saucier?"

        # Option: Buy something
        "Buy something from this mistake of humanity's hubris":
            jump vending_machine_shop

return
