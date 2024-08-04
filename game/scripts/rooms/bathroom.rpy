#
# bathroom.rpy
# OfficeSimulator
#
# Created by Atticus Young on 2/21/24.
#
#


################################################################################
## Variables
################################################################################

default bathroomRooms = ["Lobby", "Nevermind"]
image darken = "#00000088"

################################################################################
## Labels
################################################################################
## Label: bathroom #####################################################################
##
## This scene represents a bathroom. It has a background image specific to the
## bathroom and displays a dialogue box with the character 'y' asking what action
## you want to take.
##
## - If you choose "Throw Cherry bombs at the urinals", it will jump to a label
##   called "eventUrinalsFirecrackers".
##
## - If you select "Talk to the ape", it will call a function or label (apeIntro) to
##   continue the Ape questline.
##
## - If you choose "Leave", it will call the `nav_menu` function passing the
##   parameter 'bathroomRooms' to display a navigation menu for the bathroom rooms.
label bathroom:
    scene bg bathroom

    "You enter the dank and moldy bathroom"
    menu:
        "What do you want to do?"

        "Throw Cherry bombs at the urinals":
            jump eventUrinalsFirecrackers

        "Talk to the ape":
            jump apeIntro
        
        "Leave":
            call screen nav_menu(bathroomRooms)

## Label: eventUrinalsFirecrackers #####################################################
##
## This scene represents an event where you decide to throw cherry bombs at the urinals.
##
## - If you choose "{i}Do a sick flip!{/i}", it will play a sound effect for
##   throwing a firecracker, apply a shake effect to simulate the explosion, and
##   display a message that you hit the first urinal dead on.
##
## - If you select "{i}Do another flip!!{/i}", it will also play a sound effect
##   for throwing a firecracker, apply a shake effect to simulate the explosion,
##   and display a message that you nailed the other urinal.
##
## After performing the action, Jack rushes into the bathroom and reacts to your
## actions in horror. He then points at you and orders you to come to his office.

label eventUrinalsFirecrackers:  # Defining a label called 'event_urinals'
    "Despite the risk of getting fired, you procure a set of fire crackers from your pockets"
    menu:
        "{i}Do a sick flip!{/i}":
            "You push off the ground and nail a sick flip whil throwing the first Cherry Bomb"
            play audio fireCracker
            with Shake((0, 0, 0, 0), 0.5, dist=30)
            "{b}Bang!{/b}"
            "You hit the first urinal dead on"
    menu:
        "{i}Do another flip!!{/i}":
            play audio fireCracker
            with Shake((0, 0, 0, 0), 0.5, dist=30)
            "{b}Boom!!{/b}"

            "You do another flip and nail the other urinal!"
    show jack neutral  # Showing the 'jack_neutral' image
    "Jack rushes into the bathroom and gazes upon you in horror as you blow up yet another urinal"
    show jack pointing  # Showing the 'jack_pointing' image
    j "Get.{w} In.{w} My.{w} Office.{w} Now.{w}"

## bonziIntro ##########################################################################
##
## This scene represents an introduction to Bonzi, the Union Manager.
## It starts with a darkened screen and an image of Bonzi in a neutral pose.
## Bonzi greets you and reveals that he is the Union Manager forced into this company
## after the recession of 2008. He complains about his situation and jack, and mentions
## that he wants your help to move to another branch. Bonzi says that the main problem
## is that Jack which has imprisoned him here with Ancient Microwave Magic. He gives
## you a soggy list of items to find in order to help him escape.
##
## - You ask if it's illegal, he acknowledges that it would be if anyone cared about
##   legality, but the business does a lot of other illegal things that would have
##   gotten them shut down
##
## The player is then automatically taken back to the 'bathroom' label.

label bonziIntro:  # Defining a label called 'bonzi_intro'
    show darken with dissolve  # Showing the 'darken' image with dissolve effect
    show bonzi neutral  # Showing the 'bonzi_neutral' image
    # Playing an audio file
    b "Hello there, Employee"
    menu:
        "You're the ape!":
            # Playing an audio file
            b "Yes, it is I Bonzi, your Union Manager"
            # Playing an audio file
            b "After the recession of 2008 I was left without a job"
            # Playing an audio file
            b "i was forced to join this stupid company and I am now forced to do paperwork for that excuse for a kitchen utility"
            # Playing an audio file
            b "he won't even let me leave the bathroom"
            menu:
                "is there something I can do for such a famous monkey like yourself?":
                    # Playing an audio file
                    b "Why yes there is, Employee"
                    # Playing an audio file
                    b "I want out of this piss flavored hell hole"
                    # Playing an audio file
                    b "I want {i}your{/i} help moving to a different branch"
                    # Playing an audio file
                    b "The main problem is that toaster"
                    # Playing an audio file
                    show bonzi worried
                    b "He has imprisoned me here with Ancient Microwave Magic"
                    # Playing an audio file
                    b "I need you to help me escape"
                    b "I want you to steal contraband from around the office that will help me escape"
                    "The ape hands you an uncomfortably soggy list of items for you to find"
                    "Pulling your hand away, it smells of both urnine and booze"
                    "You uncomfortably slip the paper into your back pocket"
                    menu:
                        "I don't know, isn't that, y'know {i}*looks around*{/i} illegal?":
                            # Playing an audio file
                            b "Yes you ham sack. if anyone cared about legality then this buisness would have collapsed in the 70s"
                            b "Aiden's orphan consumption alone would have gotten this place shutdown before 1995"
                            b "Now I must go before they catch onto my plans"
                            b "Goodbye, Employee. I expect great results from you"
                            hide bonzi
                            $ bonzi_quest = 1  # Assigning the value 1 to the variable 'bonzi_quest'
                            "..."
                            "..."
                            "{i}What the fuck just happened?{/i}"

                            jump bathroom  # Jumping back to the 'bathroom' label

## bonziQuest ###################################################################
##
## REPLACE THE FUCKING MONKEY

label bonziQuest: # The player Helps Bonzi by collecting various unconventional items needed for the escape plan. These include items like a rubber Dildo belonging to King George the VII, a feather hat, a tub of vegan glitter, and a live chicken
    b "Ah, welcome back employee"
    b "I see you gathered the items I requested"
    b ""
