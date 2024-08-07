#
# definitions.rpy
# OfficeSimulator
#
# Created by Atticus Young on 2/21/24.
#
#

default player_name = "Employee"

## init Function #######################################################################
##
## The 'init' function is used as a global initializer in the RenPy game engine. In this
## case, it contains an 'if' statement to check if the 'who' variable is not None within
## a 'window' scope. If 'who' is not None, it creates another 'window' with the id
## "namebox", style "namebox", and text as the value of 'who' with id "who". This
## structure is followed by an commented out '# FancyText:' remark. The rest of the
## code after this comment contains a 'fancytext' statement which uses variables for
## displaying text effects. It also includes usage of the 'quick_menu' function.
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
################################################################################
## Classes and Functions
################################################################################
init python:
    import random
    
## low_beep Function ###################################################################
##
## This function is used to play a 'low beep' sound effect in the game. It takes an
## 'event' parameter and optional keyword arguments (**kwargs). If the event is set to
## "show", it plays the sound file "low_beep.ogg" on the 'sound' channel with looping
## enabled. If the event is "slow_done" or "end", it stops the sound playing on the 'sound' channel.
    def low_beep(event, **kwargs):
        if event == "show":
            renpy.music.play("soundFonts/low_beep.ogg", channel="sound", loop=True)
        elif event == "slow_done" or event == "end":
            renpy.music.stop(channel="sound")

## mid_beep Function ###################################################################
##
## This function is used to play a 'mid beep' sound effect in the game. It takes an
## 'event' parameter and optional keyword arguments (**kwargs). If the event is set to
## "show", it plays the sound corresponding to the 'midBeep' variable on the 'sound'
## channel with looping enabled. If the event is "slow_done" or "end", it stops the
## sound playing on the 'sound' channel.
    def mid_beep(event, **kwargs):
        if event == "show":
            renpy.music.play(midBeep, channel="sound", loop=True)
        elif event == "slow_done" or event == "end":
            renpy.music.stop(channel="sound")

## high_beep Function ##################################################################
##
## This function is used to play a 'high beep' sound effect in the game. It takes an
## 'event' parameter and optional keyword arguments (**kwargs). If the event is set to
## "show", it plays the sound corresponding to the 'highBeep' variable on the 'sound'
## channel with looping enabled. If the event is "slow_done" or "end", it stops the
## sound playing on the 'sound' channel.
    def high_beep(event, **kwargs):
        if event == "show":
            renpy.music.play(highBeep, channel="sound", loop=True)
        elif event == "slow_done" or event == "end":
            renpy.music.stop(channel="sound")

## microwave_beep Function #############################################################
##
## This function is used to play a 'microwave beep' sound effect in the game. It takes
## an 'event' parameter and optional keyword arguments (**kwargs). If the event is set
## to "show", it plays the sound corresponding to the 'microwaveBeep' variable on the
## 'sound' channel with looping enabled. If the event is "slow_done" or "end", it stops
## the sound playing on the 'sound' channel.
    def microwave_beep(event, **kwargs):
        if event == "show":
            renpy.music.play(microwaveBeep, channel="sound", loop=True)
        elif event == "slow_done" or event == "end":
            renpy.music.stop(channel="sound")

## narrator_Beep Function #############################################
##
## This function is used to play a 'narrator beep' sound effect in the game. It takes an 'event' parameter and optional keyword arguments (**kwargs). If the event is set to "show", it plays the sound corresponding to the 'narratorBeep' variable on the 'sound' channel with looping enabled. If the event is "slow_done" or "end", it stops the sound playing on the 'sound' channel.
    def narrator_Beep(event, **kwargs):
        if event == "show":
            renpy.music.play(narratorBeep, channel="sound", loop=True)
        elif event == "slow_done" or event == "end":
            renpy.music.stop(channel="sound")

## italian_Beep Function #############################################
##
## This function is used to play an 'italian beep' sound effect in the game. It takes an 'event' parameter and optional keyword arguments (**kwargs). If the event is set to "show", it plays the sound corresponding to the 'italianBeep' variable on the 'sound' channel with looping enabled. If the event is "slow_done" or "end", it stops the sound playing on the 'sound' channel.
    def italian_Beep(event, **kwargs):
        if event == "show":
            renpy.music.play(italianBeep, channel="sound", loop=True)
        elif event == "slow_done" or event == "end":
            renpy.music.stop(channel="sound")

## jump_random_hallway Function ########################################################
##
## This function is used to randomly select and jump to a hallway event in the game.
## It utilizes the 'random' module to generate a random number between 0 and 9,
## inclusive, and then uses this value to choose a corresponding hallway event using the
## 'renpy.jump' method.
    def jump_random_hallway():
        renpy.jump("hallway_event_%d" % random.randint(0,9))

## item Class ##########################################################################
##
## This class is used to represent an item in the game. It has four attributes: 'name', 'description', 'price' and 'sprite'. The 'name' attribute represents the name of the item, while the 'description' attribute stores a brief description of the item. The 'price' attribute sets the cost or value of the item, and 'sprite' determines the visual representation of the item.
    class item:
        def __init__(self, name, description, price, sprite):
            self.name = name
            self.description = description
            self.price = price
            self.sprite = sprite

    import math

## Shaker Class ########################################################################
##
## This class is used to create a shaking animation effect in the game. It has three
## main components: 'start' which defines the starting position, 'time' which sets the
## duration of the shake, and 'child', which represents the object or element being
## shaken.
##
## The Shaker class can be called to generate a shaking motion for a specified duration
## with optional additional properties. The resulting animation can be added to any game object to create a shaking effect.
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

## Quest Class #########################################################################
##
## This class is used to represent a specific quest in the game. It has two attributes: 'name' and 'questStageDictionary'. The 'name' attribute represents the name of the quest, while the 'questStageDictionary' attribute stores information about the different stages of the quest. The initial value for the current quest stage is set to 10.
    class quest:
        def __init__(self, name, questStageDictionary):
            self.name = name
            self.questStageDictionary = questStageDictionary
            self.currentQuestStage = 10
    
## dayTracker Class ####################################################################
##
## This class is used to track the time of day in the game. It has three attributes: 'day', 'hour', and 'minute'. The methods in this class allow for adding time and ending a day.
    class dayTracker:
        def __init__(self):
            self.day = 1
            self.hour = 9
            self.minute = 0
        
        def addTime(minutesToAdd):
            minute += minutesToAdd
            
            while minute >= 60:
                self.minute - 60
                ++self.hour
            
            if hour >= 21:
                endDay()
        
        def endDay():
            ++self.day
            renpy.jump(lobby)

## trait Class #########################################################################
##
## This class is used to represent a specific characteristic of the game. It has two attributes: 'name' and 'description'. The 'name' attribute represents the name of the trait, while the 'description' attribute stores a brief description of the trait.
    class trait:
        def __init__(self, name, description):
            self.name = name
            self.description = description
################################################################################
## Definitions
################################################################################
## displayTime Function ################################################################
##
## This function is used to display the current time. It uses information from the dayTracker class to generate a formatted string with the hours and minutes, separated by a colon. If the minute value is not zero, it includes the minutes; otherwise, it shows '00' after the colon.
    def displayTime():
        if dayTacker.minute != 0:
            return str(dayTacker.hour) + ":" + str(dayTacker.minute)
        else:
            return str(dayTacker.hour) + ":00"
# define Items #############################################
##
## This block of code is defining two items in the game using the 'define' function from RenPy. Each item definition includes parameters like name, description, value, and image file associated with it.
define deadRat = item("Dead Rat", "It's a dead rat you found in the Janitor's Closet. Why would you pick this up?", -30, "deadRatSprite.png")
define employeeID = item("Employee ID", "Your employee ID. It's made from cheap plastic and smells vaguely of dollar store Lasagna. You're pretty sure it's a stolen drivers license with the details scribbled out and a blurry picture of your face glued on.", None, "EmployeeID.png")

## define Characters ###################################################################
##
## This block of code is defining various characters in the game using the 'define' function from RenPy. Each character definition includes parameters like name, their respective callback sound effects, and other optional parameters such as color and whether 'what_slow_abortable' option is set to False.
define j = Character("Jack", what_slow_abortable=False, color="#ffffff", callback=microwave_beep)
define y = Character("You", what_slow_abortable=False, color="#ffffff")
define a = Character("Aiden", what_slow_abortable=False, color="#ffffff", callback=high_beep)
define b = Character("Bonzi", what_slow_abortable=False, color="#ffffff")
define g = Character("\"Giuseppe\"", callback=italian_Beep, what_slow_abortable=False, color="#ffffff")
define ci = Character("Officer Cast Iron", callback=italian_Beep, what_slow_abortable=False, color="#ffffff")
define s = Character("Sheryl", what_slow_abortable=False, color="#ffffff")
define ra = Character("Rat", what_slow_abortable=False, color="#ffffff")
define v = Character("Vallory The Vending Machine", what_slow_abortable=False, color="#ffffff")
define n = Character("Narrator", callback=narrator_Beep, color="#ffffff", what_slow_abortable=False)
define r = Character("Randy", callback=mid_beep, color="#ffffff", what_slow_abortable=False)

image white = "#ffffff"

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
define giuseppeTheme = "audio/music/giuseppeTheme.ogg"
define castIronTheme = "audio/music/castIronTheme.ogg"

## Sound Effects ################################################################
##
## These are definitions describing Sound Effects used during gameplay

define doorJiggle = "audio/soundEffects/doorJiggle.ogg"
define elevatorMoving = "audio/soundEffects/elevatorMoving.ogg"
define elevatorButtonClick = "audio/soundEffects/elevatorButton.ogg"
define fireCracker = "audio/soundEffects/fireCracker.ogg"
define sprayBottle = "audio/soundEffects/sprayBottle.ogg"
define giuseppeMustacheRemove = "audio/soundEffects/clothRip.ogg"
define explosion = "audio/soundEffects/explosion.ogg"


## Sound Fonts ################################################################
##
## These are definitions of the audio files used to generate sound fonts for
## NPCs when they are talking

define highBeep = "audio/soundFonts/highBeep.ogg"
define italianBeep = "audio/soundFonts/italianBeep.ogg"
define microwaveBeep = "audio/soundFonts/microwaveBeep.ogg"
define midBeep = "audio/soundFonts/midBeep.ogg"
define narratorBeep = "audio/soundFonts/narratorBeep.ogg"

################################################################################
## Variables
################################################################################
## Quest Stages ################################################################
##
## These are Dictionaries of the quest stages
define giuseppeQuestStages = {
    0: "", # Quest Failed.

    10: "Giuseppe has asked you to help bring in the other employees of the Office. Go back to him when you're ready for your first assignment.",

    20: "Giuseppe revealed himself to be a TVA agent. He needs the player to distract Sheryl and sneak behind her desk too copy her emails for evidence.",

    30: "After stealing Sheryl's emails, Giuseppe wants the player too arrest her.\n (Optional) Convince Sheryl too turn herself in too the law and help you take down the others for a reduced sentence.",

    # End of Day One

    40: "You have Arrested Sheryl and brought her to Justice. She will be tried by her people for her crimes against humanity. Return to Giuseppe and collect your next task",

    41: "Sheryl has agreed to give you information for a reduced sentence. She has revealed the only way to Defeat Aiden and Bonzi.", # If she is talked down

    50: "After defeating Sheryl, Giuseppe next needs you to bring down Randy, the Office Punching Bag. He believes him to be responsible for a disappearance yesterday and needs to be taken down quickly before he can hurt someone else.\n (Optional) Talk Randy into joining your side.",

    51: "Randy has agreed to join your side. Talk to Giuseppe about letting him help.", # If Randy is spared

    # End of Day Two

    60: "After killing Randy, Giuseppe has given you your next assignment. You need to kill Aiden and Bonzi due to their strength being too strong. Because of their immense power, you need to find out their weaknesses. He suggested checking their workspaces when they're not there.", # Aiden will not be at his workspace at 12:00 for lunch and at 4:00 for his, while Bonzi will need to be distracted by convincing him that there is a child's personal information outside in order to lure him out

    61: "Although reluctant to let Randy help due to his dangerous nature, Giuseppe lets him help due to his combat skills and his grudge against the rest of the office being a good motivator. Giuseppe has given you your next assignment. You need to kill Aiden and Bonzi due to their strength being too strong. Because of their immense power, you need to find out their weaknesses. He suggested checking their workspaces when they're not there.\n (Optional) Have Randy help you kill Aiden and Bonzi.",

    70: "I have killed Aiden, now I need to kill Bonzi.",
    71: "I have killed Aiden, now I need to kill Bonzi \n (Optional) have Randy help you kill Bonzi", # If Randy is spared and helps the player

    72: "I have killed Bonzi, now I need to kill Aiden.",
    73: "I have killed Bonzi, now I need to kill Aiden.\n (Optional) have Randy help you kill Aiden", # If Randy is spared and helps the player

    # End of Day Three

    80: "After telling Giuseppe about Aiden and Bonzi's deaths, he has made me an official TVA detective. My final objective is to arrest Jack and the 'Manager'. It will be difficult. He suggests somehow getting a copy of Jack's schedule and breaking into his office to find some sort of evidence against him.\n (Optional) Forge Evidence against Jack to have him arrested.", # If Sheryl is helping the player she can give them a copy of his schedule, if not then the player can check her computer for it. At 5 PM he will go outside to read the Economy Column of the Newspaper to de-stress.

    90: "It's a Setup! Jack has caught on to Giuseppe's scheme and sics his lawyers on you. You must defeat him!" # Giuseppe will come to the rescue of the player with his Italian powers, revealing his Italian heritage that he had hidden. If the player spared Randy he will help too.
}
## Flag #######################################################################
default canPlayerKillSherylFlag = False

## Traits #####################################################################
##
## All the possible Traits the player can have
define bloodThirsty = trait("Blood Thirsty", "You have a lust for blood and will kill anything that stands in your way.")
define charming = trait("Charming", "You're very charming and convincing. When talking to people you have more options to convince them")
define detective = trait("TVA Detective", "You're a Detective for the TVA. You have an easier time finding things around the office")

## Trait List ##################################################################
##
## The player's list of traits
default playerTraits = []

## Quest Log ###################################################################
##
## The players log of current quests.
default questLog = []

## Quests ######################################################################
##
## These are definitions describing ambience used in locations. These are things
## such as background sounds.
define giuseppeQuest = quest("In the Name of the Law", giuseppeQuestStages)

## trackers ######################################################################
##
## These are variables that keep track of things such as day or time.
define dayTacker = dayTracker()

## transform aiden_peek_1 ##############################################################
##
## This 'transform' function is used to create a visual effect for an image or character
## in the game. In this case, it defines the 'aiden_peek_1' transformation which includes
## positioning parameters like 'ypos', 'xpos', and 'rotate', as well as zoom and movement
## animations using 'linear' and 'pause' commands.
transform aiden_peek_1:
    ypos 0.1
    xpos 0.35
    rotate 50
    zoom 0.15

    linear 5 xpos 0.45

    pause 1.0

    linear 5 xpos 0.35

## transform aiden_peek_2 ##############################################################
##
## This 'transform' function is used to create a visual effect for an image or character
## in the game. It defines the 'aiden_peek_2' transformation which contains similar
## positioning parameters as well as zoom, rotation, and movement animations with
## 'linear', 'pause', and 'yoffset' commands.
transform aiden_peek_2:
    ypos 0.05
    xpos -0.1
    rotate 50
    zoom 0.35

    linear 5 xpos 0.02

    pause 1.0

    linear 5 xpos -0.1

## transform aiden_peek_3 ##############################################################
##
## This 'transform' function is used to create a visual effect for an image or character
## in the game. The 'aiden_peek_3' transformation has its own set of positioning
## parameters, complex animation movements using 'linear', 'yoffset', and 'xpos'
## commands, as well as a unique rotate animation with 'rotate' command.
transform aiden_peek_3:
    ypos 1
    yoffset -200
    xpos 0.9
    rotate 270
    zoom 0.70

    linear 8 xpos 0.5
    linear 3 xpos 0.55
    linear 5 ypos 0.1 yoffset 250

## transform aiden_reset ###############################################################
##
## This 'transform' function is used to create a visual effect for an image or character
## in the game. The 'aiden_reset' transformation resets the character's position,
## rotation, and scale by using 'ypos', 'xpos', 'rotate', and 'zoom' parameters.
transform aiden_reset:
    ypos 0
    yoffset 0
    xpos 0.2
    rotate 0
    zoom 1
