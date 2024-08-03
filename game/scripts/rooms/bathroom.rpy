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

## Bathroom ####################################################################
##
## The main handler for the Bathroom scene when they player enters.

label bathroom:
    scene bg bathroom

    "You enter the dank and moldy bathroom"
    menu:
        "What do you want to do?"

        "Throw Cherry bombs at the urinals":
            jump eventUrinalsFirecrackers

        "Talk to the ape":
            jump shop
        
        "Leave":
            call screen nav_menu(bathroomRooms)

## eventUrinalsFirecrackers #####################################################
##
## The main handler for the event where the player chooses to throw fire crackers
## at the urinals.

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

## bonziIntro ##################################################################
##
## The main handler for first meeting bonzi. This first plays upon entering the
## bathroom.

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
                    b "He has imprisoned me here with Ancient Microwave Wizardry"
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
