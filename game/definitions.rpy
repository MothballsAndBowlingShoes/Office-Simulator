#
# definitions.rpy
# OfficeSimulator
#
# Created by Atticus Young on 2/21/24.
#
#

default player_name = "Employee"
init -1:
    # FancyText: To use this say screen, you need to add the three parameters exactly as given!
    screen say(who, what, slow_effect = slow_typewriter, slow_effect_delay = 0, always_effect = None):
        style_prefix "say"

        window:
            id "window"

            if who is not None:

                window:
                    id "namebox"
                    style "namebox"
                    text who id "who"
            
            # FancyText: Here's where all the magic happens.
            # Replace your usual "text" statement with "fancytext" to enable
            # some fancy effects on text display.
            fancytext what id "what" slow_effect slow_effect slow_effect_delay slow_effect_delay always_effect always_effect
        use quick_menu

init python:
    import random
    #sound font used by characters who have a "low" voice 100hz
    def low_beep(event, **kwargs):
        if event == "show":
            renpy.music.play("soundFonts/low_beep.ogg", channel="sound", loop=True)
        elif event == "slow_done" or event == "end":
            renpy.music.stop(channel="sound")

    #sound font used by characters who have a "medium" voice, 250 hz
    def mid_beep(event, **kwargs):
        if event == "show":
            renpy.music.play(midBeep, channel="sound", loop=True)
        elif event == "slow_done" or event == "end":
            renpy.music.stop(channel="sound")

    #sound font used by characters who have a "high" voice 500 hz
    def high_beep(event, **kwargs):
        if event == "show":
            renpy.music.play(highBeep, channel="sound", loop=True)
        elif event == "slow_done" or event == "end":
            renpy.music.stop(channel="sound")

    #sound font used by Jack, specifically made of Microwave beeps
    def microwave_beep(event, **kwargs):
        if event == "show":
            renpy.music.play(microwaveBeep, channel="sound", loop=True)
        elif event == "slow_done" or event == "end":
            renpy.music.stop(channel="sound")

    #sound font used by the narrator for non-speaker text, 500 hz with sawtooth wave
    def narrator_Beep(event, **kwargs):
        if event == "show":
            renpy.music.play(narratorBeep, channel="sound", loop=True)
        elif event == "slow_done" or event == "end":
            renpy.music.stop(channel="sound")

    #sound font used by the Giuseppe when he talks, specifically made for him using Kevin Macleod's song "Bushwick Tarantella Loop"
    def italian_Beep(event, **kwargs):
        if event == "show":
            renpy.music.play(italianBeep, channel="sound", loop=True)
        elif event == "slow_done" or event == "end":
            renpy.music.stop(channel="sound")

    # Function that jumps to a random hallway label
    def jump_random_hallway():
        renpy.jump("hallway_event_%d" % random.randint(0,9))

    class item:
        def __init__(self, name, description, price, sprite):
            self.name = name
            self.description = description
            self.price = price
            self.sprite = sprite

    import math

    class Shaker(object):

        anchors = {
            'top' : 0.0,
            'center' : 0.5,
            'bottom' : 1.0,
            'left' : 0.0,
            'right' : 1.0,
            }

        def __init__(self, start, child, dist):
            if start is None:
                start = child.get_placement()
            #
            self.start = [ self.anchors.get(i, i) for i in start ]  # central position
            self.dist = dist    # maximum distance, in pixels, from the starting point
            self.child = child

        def __call__(self, t, sizes):
            # Float to integer... turns floating point numbers to
            # integers.
            def fti(x, r):
                if x is None:
                    x = 0
                if isinstance(x, float):
                    return int(x * r)
                else:
                    return x

            xpos, ypos, xanchor, yanchor = [ fti(a, b) for a, b in zip(self.start, sizes) ]

            xpos = xpos - xanchor
            ypos = ypos - yanchor

            nx = xpos + (1.0-t) * self.dist * (renpy.random.random()*2-1)
            ny = ypos + (1.0-t) * self.dist * (renpy.random.random()*2-1)

            return (int(nx), int(ny), 0, 0)

    def _Shake(start, time, child=None, dist=100.0, **properties):

        move = Shaker(start, child, dist=dist)

        return renpy.display.layout.Motion(move,
                    time,
                    child,
                    add_sizes=True,
                    **properties)

    Shake = renpy.curry(_Shake)

#
# Items
#
define deadRat = item("Dead Rat", "It's a dead rat you found in the Janitor's Closet. Why would you pick this up?", -30, "deadRatSprite.png")
define employeeID = item("Employee ID", "Your employee ID. It's made from cheap plastic and smells vaguely of dollar store Lasagna. You're pretty sure it's a stolen drivers license with the details scribbled out and a blurry picture of your face glued on.", None, "EmployeeID.png")

#
# Character defintions
#

define j = Character("Jack", what_slow_abortable=False, color="#ffffff", callback=microwave_beep)
define y = Character("You", what_slow_abortable=False, color="#ffffff")
define a = Character("Aiden", what_slow_abortable=False, color="#ffffff", callback=high_beep)
define b = Character("Bonzi", what_slow_abortable=False, color="#ffffff")
define g = Character("Giuseppe", what_slow_abortable=False, color="#ffffff")
define s = Character("Sheryl", what_slow_abortable=False, color="#ffffff")
define ra = Character("Rat", what_slow_abortable=False, color="#ffffff")
define v = Character("Vallory The Vending Machine", what_slow_abortable=False, color="#ffffff")
define n = Character("Narrator", callback=narrator_Beep, color="#ffffff", what_slow_abortable=False)
define r = Character("Randy", callback=mid_beep, color="#ffffff", what_slow_abortable=False)


################################################################################
## Sound Defintions
################################################################################

## Ambience ####################################################################
##
## These are definitions describing ambience used in locations. These are things
## such as background sounds.

define backroomsAmbience = "audio/ambience/backroomsAmbience.ogg"
define elevatorAmbience = "audio/ambience/elevatorAmbience.ogg"
define hallwayAmbience = "audio/ambience/hallwayAmbience.ogg"

## Music #######################################################################
##
## These are definitions describing Music. These can be characters or locations.

define valloryTheme = "audio/music/valloryTheme.ogg"
define aidenTheme = "audio/music/aidenTheme.ogg"
define dayOneTheme = "audio/music/theme1.ogg"
define dayTwoTheme = "audio/music/valloryTheme.ogg"

## Sound Effects ################################################################
##
## These are definitions describing Sound Effects used during gameplay

define doorJiggle = "audio/soundEffects/doorJiggle.ogg"
define elevatorMoving = "audio/soundEffects/elevatorMoving.ogg"
define elevatorButtonClick = "audio/soundEffects/elevatorButton.ogg"
define fireCracker = "audio/soundEffects/fireCracker.ogg"
define sprayBottle = "audio/soundEffects/sprayBottle.ogg"

## Sound Fonts ################################################################
##
## These are definitions of the audio files used to generate sound fonts for
## NPCs when they are talking

define highBeep = "audio/soundFonts/highBeep.ogg"
define italianBeep = "audio/soundFonts/italianBeep.ogg"
define microwaveBeep = "audio/soundFonts/microwaveBeep.ogg"
define midBeep = "audio/soundFonts/midBeep.ogg"
define narratorBeep = "audio/soundFonts/narratorBeep.ogg"

transform aiden_peek_1:
    ypos 0.1
    xpos 0.35
    rotate 50
    zoom 0.15

    linear 5 xpos 0.45

    pause 1.0

    linear 5 xpos 0.35

transform aiden_peek_2:
    ypos 0.05
    xpos -0.1
    rotate 50
    zoom 0.35

    linear 5 xpos 0.02

    pause 1.0

    linear 5 xpos -0.1

transform aiden_peek_3:
    ypos 1
    yoffset -200
    xpos 0.9
    rotate 270
    zoom 0.70

    linear 8 xpos 0.5
    linear 3 xpos 0.55
    linear 5 ypos 0.1 yoffset 250

transform aiden_reset:
    ypos 0
    yoffset 0
    xpos 0.2
    rotate 0
    zoom 1

transform text_effect:
    parallel:
        block:
            linear 0.1 xoffset -2 yoffset 2
            linear 0.1 xoffset 3 yoffset -3
            linear 0.1 xoffset 2 yoffset -2
            linear 0.1 xoffset -3 yoffset 3
            linear 0.1 xoffset 0 yoffset 0
            repeat
    parallel:
        block:
            alpha .2
            linear 1.0 alpha .9
            linear 1.0 alpha .2
            repeat
