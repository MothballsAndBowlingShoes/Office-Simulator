default first_visit = 0  # Setting a default value for the variable 'first_visit'

#define bonzi_disapear  # Defining a label called 'bonzi_disapear'

image darken = "#00000088"  # Declaring an image variable with a color value

$ first_visit = 0  # Setting the value of 'first_visit' to 0
$ bonzi_quest_update = false;

label bathroom:  # Defining a label called 'bathroom'
    scene bathroom  # Displaying the bathroom scene

    "You enter the dank and moldy bathroom"

    if first_visit == 0:  # Checking if the variable 'first_visit' is equal to 0
        jump bonzi_intro  # Jumping to the label 'bonzi_intro' if the condition is true

    menu:
        "What do you want to do?"

        "Throw Cherry bombs at the urinals":
            jump event_urinals  # Jumping to the label 'event_urinals' if selected

label bonzi_intro:  # Defining a label called 'bonzi_intro'
    show darken with dissolve  # Showing the 'darken' image with dissolve effect
    show bonzi_neutral  # Showing the 'bonzi_neutral' image
    voice "bonzi_1.wav"  # Playing an audio file
    b "Hello there, Employee"  # Displaying text
    menu:
        "your the ape!":
            voice "bonzi_2.wav"  # Playing an audio file
            b "Yes, it is I Bonzi, your Union Manager"  # Displaying text
            voice "bonzi_3.wav"  # Playing an audio file
            b "After the recession of 2008 I was left without a job"  # Displaying text
            voice "bonzi_4.wav"  # Playing an audio file
            b "i was forced to join this stupid company and I am now forced to do paperwork for that excuse for a kitchen utility"  # Displaying text
            voice "bonzi_5.wav"  # Playing an audio file
            b "he won't even let me leave the bathroom"  # Displaying text
            menu:
                "is there something I can do for such a famous monkey like yourself?":
                    voice "bonzi_6.wav"  # Playing an audio file
                    b "Why yes there is, Employee"  # Displaying text
                    voice "bonzi_7.wav"  # Playing an audio file
                    b "I want out of this piss flavored hell hole"  # Displaying text
                    voice "bonzi_8.wav"  # Playing an audio file
                    b "I want {i}your{/i} help moving to a different branch"  # Displaying text
                    voice "bonzi_9.wav"  # Playing an audio file
                    b "The main problem is that toaster"  # Displaying text
                    voice "bonzi_10.wav"  # Playing an audio file
                    b "He keeps witholding my request for a transfer"  # Displaying text
                    voice "bonzi_11.wav"  # Playing an audio file
                    b "i want you to forge his signature and have me moved anywhere else but here"  # Displaying text
                    menu:
                        "i don't know, isn't that, y'know {i}looks around{/i} illegal?":
                            voice "bonzi_12.wav"  # Playing an audio file
                            b "yes you ham sack. if anyone cared about legality then this buisness would have collapsed in the 70s"  # Displaying text
                            b "Now I must go before they catch onto my plans"  # Displaying text
                            b "Goodbye, Employee. I expect great results from you"  # Displaying text

                            $ bonzi_quest = 1  # Assigning the value 1 to the variable 'bonzi_quest'
                            $ first_visit = 1  # Assigning the value 1 to the variable 'first_visit'
                            "..."  # Displaying text
                            "..."  # Displaying text
                            "{i}What the fuck just happened?{/i}"  # Displaying text

                            jump bathroom  # Jumping back to the 'bathroom' label

label event_urinals:  # Defining a label called 'event_urinals'
    "Despite the risk of getting fired, you procure a set of fire crackers from your pockets"  # Displaying text
    menu:
        "{i}Do a sick flip!{/i}":
            "You push off the ground and nail a sick flip whil throwing the first Cherry Bomb"  # Displaying text
            "{b}Bang!{/b}"  # Displaying text
            with Shake((0, 0, 0, 0), 0.5, dist=30)  # Applying a Shake effect
            "You hit the first urinal dead on"  # Displaying text
    menu:
        "{i}Do another flip!!{/i}":
            "{b}Boom!!{/b}"  # Displaying text
            with Shake((0, 0, 0, 0), 0.5, dist=30)  # Applying a Shake effect
            "You do another flip and nail the other urinal!"  # Displaying text
    show jack_neutral  # Showing the 'jack_neutral' image
    "Jack rushes into the bathroom and gazes upon you in horror as you blow up yet another urinal"  # Displaying text
    show jack_pointing  # Showing the 'jack_pointing' image
    j "Get. In. My. Office. Now."  # Displaying text