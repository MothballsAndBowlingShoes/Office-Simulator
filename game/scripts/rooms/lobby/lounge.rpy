define i = Character("Aiden")

label lounge:
    play music dayOneTheme

    scene bg lounge
    menu:

        "What should I do?"



        "talk to ":

            show aiden
            a "Bask in me shining glory!"
            menu:
                "What should I Do"

                "Talk to the poor man":
                    a "On raglan road on an autumn day, i saw 'er first an' knew that 'er dark 'air wud weave a snare that oi may wan day rue."

                "Leave while you still have some eyes left in your skull":
                    "Aiden Store Jump"



    return
