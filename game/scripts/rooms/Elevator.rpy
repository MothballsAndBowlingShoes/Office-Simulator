#
# Elevator.rpy
# OfficeSimulator
#
# Created by Atticus Young on 2/21/24.
#
#
init python:
    currentFloor = 2

    def leaveRoom():
        if currentFloor==0:
            renpy.jump("parkingGarage")
        if currentFloor==1:
            renpy.jump("lobby")
        if currentFloor== 2:
            renpy.jump("hallway")

label elevator:
    scene elevator
    play music "music/ambience_elevator.mp3"
    jump elevatorMenu

label elevatorMenu:
    menu:
        y "What would you like to do?"

        "Go to another Floor":
            menu:
                y "What floor should I go to?"

                "Floor 2":
                    $ currentFloor = 2
                    play sound "soundClips/elevator_buttonClick.mp3"
                    $ renpy.pause(0.5, hard=True)

                    play sound "soundClips/elevator_moving.ogg"
                    $ renpy.pause(0.650, hard=True)
                    with Shake((0, 0, 0, 0), 2.875, dist=5)
                    $ renpy.pause(8.360, hard=True)
                    with Shake((0, 0, 0, 0), 2.765, dist=5)
                    jump elevator

                "Floor 1":
                    $ currentFloor = 1
                    play sound "soundClips/elevator_buttonClick.mp3"
                    $ renpy.pause(0.5, hard=True)

                    play sound "soundClips/elevator_moving.ogg"
                    $ renpy.pause(0.650, hard=True)
                    with Shake((0, 0, 0, 0), 2.875, dist=5)
                    $ renpy.pause(8.360, hard=True)
                    with Shake((0, 0, 0, 0), 2.765, dist=5)
                    jump elevator

                "Basement":
                    $ currentFloor = 0
                    play sound "soundClips/elevator_buttonClick.mp3"
                    $ renpy.pause(0.5, hard=True)

                    play sound "soundClips/elevator_moving.ogg"
                    $ renpy.pause(0.650, hard=True)
                    with Shake((0, 0, 0, 0), 2.875, dist=5)
                    $ renpy.pause(8.360, hard=True)
                    with Shake((0, 0, 0, 0), 2.765, dist=5)
                    jump elevator
        
        "Leave":
            $ leaveRoom()