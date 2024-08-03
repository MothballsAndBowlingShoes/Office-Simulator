#
# elevator.rpy
# OfficeSimulator
#
# Created by Atticus Young on 2/21/24.
#
#

################################################################################
## Variables
################################################################################
default currentFloor = 2

## leaveRoom #####################################################################
##
## This function is used to simulate leaving a room based on the current floor. If
## the current floor is 0, it will jump to the "parkingGarage". If the current
## floor is 1, it will jump to the "lobby". Otherwise, it will jump to the "hallway".
## The function does not take any arguments.
init python:
    def leaveRoom():
        if currentFloor==0:
            renpy.jump("parkingGarage")
        if currentFloor==1:
            renpy.jump("lobby")
        else:
            renpy.jump("hallway")

## moveElevator ####################################################################
##
## This function is responsible for moving the elevator to the target floor. It
## plays several sounds and uses shakes and pauses to simulate the movement of an
## elevator. The function takes one parameter, which is the target floor that the
## user wants to go to.
init python:
    def moveElevator(targetFloor):
        currentFloor = targetFloor
        renpy.play(elevatorButtonClick)
        renpy.pause(0.5, hard=True)
        renpy.play(elevatorMoving)
        renpy.pause(0.650, hard=True)
        renpy.with_statement(Shake((0, 0, 0, 0), 2.875, dist=5), True)
        renpy.pause(8.360, hard=True)
        renpy.with_statement(Shake((0, 0, 0, 0), 2.765, dist=5), True)

################################################################################
## Labels
################################################################################

## elevator ####################################################################
##
## This scene represents the interior of an elevator. It has a background image
## specific to the elevator and plays the elevatorAmbience music. There's a
## dialogue box with the character 'y' asking what action you want to take.
##
## If you choose "Go to another Floor", it will present three options: "Floor 2",
## "Floor 1" or "Basement". After selecting an option, it will move the elevator
## using the `moveElevator` function and repeat this scene (jump elevator).
##
## If you select "Leave", it will call the `leaveRoom` function to simulate
## leaving the room based on the current floor.
label elevator:
    scene bg elevator
    play music elevatorAmbience
    y "What would you like to do?"

    "Go to another Floor":
        menu:
            y "What floor should I go to?"

            "Floor 2":
                $ moveElevator(2)
                jump elevator

            "Floor 1":
                $ moveElevator(1)
                jump elevator

            "Basement":
                $ moveElevator(0)
                jump elevator
    
    "Leave":
        $ leaveRoom()
