#
# lobby.rpy
# OfficeSimulator
#
# Created by Atticus Young on 2/21/24.
#
#

default lobbyRooms = ["Bathroom", "Elevator", "Janitor"]

label lobbyMenu:
"What do you want to do?"
menu:
    "Talk to the Moose Woman":
        return
    "Go Somewhere?":
        call screen nav_menu(lobbyRooms)

label lobby:
    scene bg lobby
    play music dayOneTheme
    jump lobbyMenu

return
