#
# lobby.rpy
# OfficeSimulator
#
# Created by Atticus Young on 2/21/24.
#
#

label lobby:

    scene lobby

    "What do you want to do?"
    menu:
        "Talk to the Moose Woman":
            return
        "Go Somewhere?":
            call nav_menu

return
