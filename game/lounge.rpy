define i = Character("irish")

label lounge:
    play music "day1.mp3"

    scene lounge
    menu:

        "What should I do?"

        

        "talk to ":
            
            show aiden
            i "Bask in me shining glory!"
            menu:
                "What should I Do"

                "Talk to the poor fecker":
                    voice "irish2.mp3"
                    "On raglan road on an autumn day, i saw 'er first an' knew that 'er dark 'air wud weave a snare that oi may wan day rue."

                "Leave while you still have your eyes left in your skull":
                    jump lounge



    return
