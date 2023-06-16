default first_visit = 0  # Setting a default value for the variable 'first_visit'

image darken = "#00000088"  # Declaring an image variable with a color value

$ bonzi_quest_stage = 0  # Setting the value of 'first_visit' to 0
$ bonzi_quest_update = false;

label bonzi_intro:  # Defining a label called 'bonzi_intro'
    show darken with dissolve  # Showing the 'darken' image with dissolve effect
    show bonzi_neutral  # Showing the 'bonzi_neutral' image
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
                    b "He keeps witholding my request for a transfer"  
                    voice "bonzi_11.wav"  # Playing an audio file
                    b "i want you to forge his signature and have me moved anywhere else but here"  
                    menu:
                        "i don't know, isn't that, y'know {i}looks around{/i} illegal?":
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

label bonzi_quest0:
