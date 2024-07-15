#
# definitions.rpy
# OfficeSimulator
#
# Created by Atticus Young on 2/21/24.
#
#

init python:
    #sound font used by characters who have a "low" voice 100hz
    def low_beep(event, **kwargs):
        if event == "show":
            renpy.music.play("soundFonts/low_beep.ogg", channel="sound", loop=True)
        elif event == "slow_done" or event == "end":
            renpy.music.stop(channel="sound")

    #sound font used by characters who have a "medium" voice, 250 hz
    def mid_beep(event, **kwargs):
        if event == "show":
            renpy.music.play("soundFonts/mid_beep.ogg", channel="sound", loop=True)
        elif event == "slow_done" or event == "end":
            renpy.music.stop(channel="sound")

    #sound font used by characters who have a "high" voice 500 hz
    def high_beep(event, **kwargs):
        if event == "show":
            renpy.music.play("soundFonts/high_beep.ogg", channel="sound", loop=True)
        elif event == "slow_done" or event == "end":
            renpy.music.stop(channel="sound")

    #sound font used by Jack, specifically made of Microwave beeps
    def microwave_beep(event, **kwargs):
        if event == "show":
            renpy.music.play("soundFonts/microwave_beep.ogg", channel="sound", loop=True)
        elif event == "slow_done" or event == "end":
            renpy.music.stop(channel="sound")

    #sound font used by the narrator for non-speaker text, 500 hz with sawtooth wave
    def narrator_Beep(event, **kwargs):
        if event == "show":
            renpy.music.play("soundFonts/narrator_beep.ogg", channel="sound", loop=True)
        elif event == "slow_done" or event == "end":
            renpy.music.stop(channel="sound")

    #sound font used by the Giuseppe when he talks, specifically made for him using Kevin Macleod's song "Bushwick Tarantella Loop"
    def italian_Beep(event, **kwargs):
        if event == "show":
            renpy.music.play("soundFonts/italian_beep.ogg", channel="sound", loop=True)
        elif event == "slow_done" or event == "end":
            renpy.music.stop(channel="sound")

    class item:
        def __init__(self, name, description, price):
            self.name = name
            self.description = description
            self.price = price

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

define deadRat = item("Dead Rat", "It's a dead rat you found in the Janitor's Closet. Why would you pick this up?", -30)

define j = Character("Jack", what_slow_abortable=False, color="#ffffff", callback=microwave_beep)
define y = Character("You", what_slow_abortable=False, color="#ffffff")
define a = Character("Aiden", what_slow_abortable=False, color="#ffffff", callback=high_beep)
define b = Character("Bonzi", what_slow_abortable=False, color="#ffffff")
define g = Character("Giuseppe", what_slow_abortable=False, color="#ffffff")
define s = Character("Sheryl", what_slow_abortable=False, color="#ffffff")
define r = Character("Rat", what_slow_abortable=False, color="#ffffff")
define v = Character("Vallory The Vending Machine", what_slow_abortable=False, color="#ffffff")
define n = Character("Narrator", callback=narrator_Beep, color="#ffffff", what_slow_abortable=False)
