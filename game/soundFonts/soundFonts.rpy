init python:
    #sound font used by characters who have a "low" voice 100hz
    def low_beep(event, **kwargs):
        if event == "show":
            renpy.music.play("low_beep.ogg", channel="sound", loop=True)
        elif event == "slow_done" or event == "end":
            renpy.music.stop(channel="sound")

    #sound font used by characters who have a "medium" voice, 250 hz
    def mid_beep(event, **kwargs):
        if event == "show":
            renpy.music.play("mid_beep.ogg", channel="sound", loop=True)
        elif event == "slow_done" or event == "end":
            renpy.music.stop(channel="sound")

    #sound font used by characters who have a "high" voice 500 hz
    def high_beep(event, **kwargs):
        if event == "show":
            renpy.music.play("high_beep.ogg", channel="sound", loop=True)
        elif event == "slow_done" or event == "end":
            renpy.music.stop(channel="sound")

    #sound font used by Jack, specifically made of Microwave beeps
    def microwave_beep(event, **kwargs):
        if event == "show":
            renpy.music.play("microwave_beep.ogg", channel="sound", loop=True)
        elif event == "slow_done" or event == "end":
            renpy.music.stop(channel="sound")

    #sound font used by the narrator for non-speaker text, 500 hz with sawtooth wave
    def narrator_Beep(event, **kwargs):
        if event == "show":
            renpy.music.play("narrator_beep.ogg", channel="sound", loop=True)
        elif event == "slow_done" or event == "end":
            renpy.music.stop(channel="sound")

    #sound font used by the Giuseppe when he talks, specifically made for him using Kevin Macleod's song "Bushwick Tarantella Loop"
    def italian_Beep(event, **kwargs):
        if event == "show":
            renpy.music.play("italian_beep.ogg", channel="sound", loop=True)
        elif event == "slow_done" or event == "end":
            renpy.music.stop(channel="sound")

