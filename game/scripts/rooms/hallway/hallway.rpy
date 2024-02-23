#
# hallway.rpy
# OfficeSimulator
#
# Created by Atticus Young on 2/21/24.
#
#

label hallway:
    scene hallway
    y "What should I do?"
    menu:
        "Management's office":
            jump mg
        "Go farther down the hallway":
            jump never_ending_hallway_event_manager
        "Use the vending machine":
            jump hallway_vendingMachine
    return
