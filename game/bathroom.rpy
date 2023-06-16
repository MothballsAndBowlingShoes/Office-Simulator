label bathroom:  # Defining a label called 'bathroom'
    scene bathroom  # Displaying the bathroom scene

    "You enter the dank and moldy bathroom"
    if bonzi_quest_stage == 0:  # Checking if the variable 'first_visit' is equal to 0
        jump bonzi_intro  # Jumping to the label 'bonzi_intro' if the condition is true
        python:
            bonzi_quest_stage += 1
    elif bonzi_quest_stage == 1 && bonzi_quest_update == true:
        jump bonzi_quest0
        python:
            bonzi_quest_stage += 1
            bonzi_quest_update = false

    menu:
        "What do you want to do?"

        "Throw Cherry bombs at the urinals":
            jump event_urinals  # Jumping to the label 'event_urinals' if selected

label event_urinals:  # Defining a label called 'event_urinals'
    "Despite the risk of getting fired, you procure a set of fire crackers from your pockets"  
    menu:
        "{i}Do a sick flip!{/i}":
            "You push off the ground and nail a sick flip whil throwing the first Cherry Bomb"  
            "{b}Bang!{/b}"  
            with Shake((0, 0, 0, 0), 0.5, dist=30)  # Applying a Shake effect
            "You hit the first urinal dead on"  
    menu:
        "{i}Do another flip!!{/i}":
            "{b}Boom!!{/b}"  
            with Shake((0, 0, 0, 0), 0.5, dist=30)  # Applying a Shake effect
            "You do another flip and nail the other urinal!"  
    show jack_neutral  # Showing the 'jack_neutral' image
    "Jack rushes into the bathroom and gazes upon you in horror as you blow up yet another urinal"  
    show jack_pointing  # Showing the 'jack_pointing' image
    j "Get. In. My. Office. Now."  

default first_visit = 0  # Setting a default value for the variable 'first_visit'

image darken = "#00000088"  # Declaring an image variable with a color value

$ bonzi_quest_stage = 0  # Setting the value of 'first_visit' to 0
$ bonzi_quest_update = false;

label bonzi_intro:  # Defining a label called 'bonzi_intro'
    show darken with dissolve  # Showing the 'darken' image with dissolve effect
    show bonzi neutral  # Showing the 'bonzi_neutral' image
    voice "bonzi_1.wav"  # Playing an audio file
    b "Hello there, Employee"  
    menu:
        "You're the ape!":
            voice "bonzi_2.wav"  # Playing an audio file
            b "Yes, it is I Bonzi, your Union Manager"  
            voice "bonzi_3.wav"  # Playing an audio file
            b "After the recession of 2008 I was left without a job"  
            voice "bonzi_4.wav"  # Playing an audio file
            b "i was forced to join this stupid company and I am now forced to do paperwork for that excuse for a kitchen utility"  
            voice "bonzi_5.wav"  # Playing an audio file
            b "he won't even let me leave the bathroom"  
            menu:
                "is there something I can do for such a famous monkey like yourself?":
                    voice "bonzi_6.wav"  # Playing an audio file
                    b "Why yes there is, Employee"  
                    voice "bonzi_7.wav"  # Playing an audio file
                    b "I want out of this piss flavored hell hole"  
                    voice "bonzi_8.wav"  # Playing an audio file
                    b "I want {i}your{/i} help moving to a different branch"  
                    voice "bonzi_9.wav"  # Playing an audio file
                    b "The main problem is that toaster"  
                    voice "bonzi_10.wav"  # Playing an audio file
                    show bonzi worried
                    b "He has imprisoned me here with Ancient Microwave Wizardry"  
                    voice "bonzi_11.wav"  # Playing an audio file
                    b "I need you to help me escape"  
                    menu:
                        "I don't know, isn't that, y'know {i}*looks around*{/i} illegal?":
                            voice "bonzi_12.wav"  # Playing an audio file
                            b "Yes you ham sack. if anyone cared about legality then this buisness would have collapsed in the 70s"  
                            b "Aiden's orphan consumption alone would have gotten this place shutdown before 1995"
                            b "Now I must go before they catch onto my plans"  
                            b "Goodbye, Employee. I expect great results from you"  

                            $ bonzi_quest = 1  # Assigning the value 1 to the variable 'bonzi_quest'
                            $ first_visit = 1  # Assigning the value 1 to the variable 'first_visit'
                            "..."  
                            "..."  
                            "{i}What the fuck just happened?{/i}"  

                            jump bathroom  # Jumping back to the 'bathroom' label

label bonzi_quest0: #Help Bonzi Buddy by collecting various unconventional items needed for the escape plan. These may include items like a rubber Dildo, a feather hat belonging to King George the VII, a tub of glitter, and a live chicken
    b "Ah, welcome back employee"
    b "I see you gathered the items i require"
