default first_visit = 0

#define bonzi_disapear
    

image darken = "#00000088"
$ first_visit = 0

label bathroom:
    scene bathroom
    

    "You enter the dank and moldy bathroom"
    
    if first_visit == 0:
        jump bonzi_intro
    
    menu: 
        "What do you want to do?"

        "Throw Cherry bombs at the urinals":
            jump event_urinals

        #"Talk to the ape":
            #jump Bonzi

label bonzi_intro:
    show darken with dissolve
    show bonzi_neutral
    voice "bonzi_1.wav"
    b "Hello there, Employee"
    menu:
        "your the ape!":
            voice "bonzi_2.wav"
            b "Yes, it is I Bonzi, your Union Manager"
            voice "bonzi_3.wav"
            b "After the recession of 2008 I was left without a job"
            voice "bonzi_4.wav"
            b "i was forced to join this stupid company and I am now forced to do paperwork for that excuse for a kitchen utility"
            voice "bonzi_5.wav"
            b "he won't even let me leave the bathroom"
            menu:
                "is there something I can do for such a famous monkey like yourself?":
                    voice "bonzi_6.wav"
                    b "Why yes there is, Employee"
                    voice "bonzi_7.wav"
                    b "I want out of this piss flavored hell hole"
                    voice "bonzi_8.wav"
                    b "I want {i}your{/i} help moving to a different branch"
                    voice "bonzi_9.wav"
                    b "The main problem is that toaster"
                    voice "bonzi_10.wav"
                    b "He keeps witholding my request for a transfer"
                    voice "bonzi_11.wav"
                    b "i want you to forge his signature and have me moved anywhere else but here"
                    menu:
                        "i don't know, isn't that, y'know {i}looks around{/i} illegal?":
                            voice "bonzi_12.wav"
                            b "yes you ham sack. if anyone cared about legality then this buisness would have collapsed in the 70s"
                            b "Now I must go before they catch onto my plans"
                            show bonzi_neutral:
                                linear 1.0 xzoom -1.0 ypos -1.0
                                linear 1.0 xzoom 1.0
                                repeat
                            b "Goodbye, Employee. I expect great results from you"

                            $ bonzi_quest = 1
                            $ first_visit = 1
                            "..."
                            "..."
                            "{i}What the fuck just happened?{/i}"

                            jump bathroom

label event_urinals:
    "Despite the risk of getting fired, you procure a set of fire crackers from your pockets"
    menu:
        "{i}Do a sick flip!{/i}":
            "You push off the ground and nail a sick flip whil throwing the first Cherry Bomb"
            "{b}Bang!{/b}"
            with Shake((0, 0, 0, 0), 0.5, dist=30)
            "You hit the first urinal dead on"
    menu:
        "{i}Do another flip!!{/i}":
            "{b}Boom!!{/b}"
            with Shake((0, 0, 0, 0), 0.5, dist=30)
            "You do another flip and nail the other urinal!"
    show jack_neutral
    "Jack rushes into the bathroom and gazes upon you in horror as you blow up yet another urinal"
    show jack_pointing
    j "Get. In. My. Office. Now."