label start:
    scene lobby
    play music "day1.mp3"
    show jack neutral
    j "Welcome to your {i}new{/i} and {i}mostly{/i} unpaid and illegal job"
    menu:
        "Isn't there a process to these things?":
            j "No"
            j "You're hired"
            j "No questions asked"
        "Wow, the government just sanctions you not paying us?":
            j "You'd be surprised how much you can get away with when you have a nuclear arsenal to rival the country of Turkey"
    j "I'm the staff manager, Jack"
    j "We have been short on staff ever since everyone else was blinded by Aiden's reflective Irish skin, so it's a miracle you came when you did."
    j "What few Slave labor we have has been consumed by {i}The Hallway{/i}"
    menu:
        "Is your head a microwave?":
            j "Yes"
            j "My father was a Panasonic HomeCook MM-GN08KP"
            j "He was one of the few microwaves I was proud to know"
            j "He liberated the country of Texas from its tyrannical communist oppressors and ushered in an age of capitalist utopia"

            menu:
                "What about your mother?":
                    j "Employee..."
                    j "WE DO NOT TALK ABOUT MY DIRTY COMMUNIST MOTHER, DO YOU UNDERSTAND ME?"
                    menu:
                        "Yes, sir...":
                            "The man with a microwave for a head shakes it in disappointment"
                            jump tour_lobby


        "Wait, blinded?":
            j "Who said anything about blinded?"
            y "You di-"
            jump tour_lobby
        "Wow! you guys have hallways? Not even the McDonalds i worked at could afford those!":
            j "Yep, We even have complementary rats"

label tour_lobby:
    j "Anyways, let me give you the tour"
    j "This here is the lobby"
    j "This is where we put up our corporate front to throw the unsuspecting federal agents off our trail"
    j "If you listen closely, you can hear the POW's screams from the {i}pit{/i}"
    jump tour_elevator

label tour_elevator:
    scene elevator
    with fade
    show jack neutral
    j "This here is the elevator, your local hub for navigating around the building"
    j "{i}Ignore the smell of sweat and dried blood; we still haven't cleaned up after the janitorial department's unsupervised orgy last week{/i}"
    j "Also"
    j "If you hear any creaking coming from the shaft, just stay calm, and remember our company motto:"
    show jack pointing
    j "{i}You're easily expendable, and you will be replaced within the first 10 hours{/i}"
    menu:
        "Wow, don't you think that motto is rather harsh?":
            j "You would be surprised how many people kill themselves thinking they can get out of work"
            jump tour_lounge

label tour_lounge:
    scene lounge
    play music "day1.mp3"
    show jack neutral

    j "This here is the employee lounge"
    j "This is where you can relax after a day of hard work"
    j "It's also where you will sleep"
    j "As if by some video game logic, just lying in one of the beds will skip you ahead to the next day!"

    menu:
        "Can't I sleep at home?":
            show jack neutral
            with Shake((0, 0, 0, 0), 0.5, dist=30)
            j "NO! ONCE YOU ENTER HERE, THERE IS NO LEAVING!"
            with Shake((0, 0, 0, 0), 0.5, dist=30)
            j "I HAVEN'T SEEN MY WIFE AND KIDS IN 12 YEARS!"
            ##show jack neutral
            with Shake((0, 0, 0, 0), 0.5, dist=30)
            "The crazy microwave man backs you into a corner"
            j "Ohhhhhh"
            j "LITTLE TIMMY IS PROBABLY A FULL GROWN MAN BY NOW!"
            with Shake((0, 0, 0, 0), 0.5, dist=30)
            "{i}He grabs your shoulders and starts shaking you{/i}"

        "What about food?":
            j "You can run down to the local McDonald's or eat the roaches off the floor; either one works"
            show jack neutral:
                zoom 2.0 yalign 0.1 xalign -0.5 rotate -30
            j "{i}If I were you, I know which one I would choose{/i}"
            show jack neutral:
                zoom 1.0 yalign 0.0 xalign 0.5 rotate 0
            menu:
                "Can I use your head to cook my food?":
                    j "Please don't"
                    j "Last time that happened, it took a week to clean all that lasagna"
                    j "{i}I can still taste Dave's pasta sauce{/i}"
                    "{i}He shudders{/i}"
                    jump tour_boardroom

label tour_boardroom:
    scene boardroom
    show jack neutral
    j "This is the boardroom!"
    j "Here, we host daily briefings on company updates that range from {i}helpful{/i} to {i}not helpful at all{/i}"
    j "This is also where Aiden sells his goods"
    show jack neutral:
        ease 1 left
    show aiden:
        right
    with moveinright
    a "Bask in my pale skin in its blinding glory"
    j "Try to avoid staring at him for too long..."
    j "{i}It didn't turn out to well for the last guy who did it...{/i}"
    j "Also, anything you hear from police reports about him consuming families is purely rumor and speculation... \n{i}probably{/i}..."
    hide aiden
    show jack neutral:
    j "He will sell you objects you might need in exchange for our new cryptocurrency"
    j "{b}Office Coin{/b}"
    menu:
        "Do you accept the fiscal monetary standard established in 1792 by this fine nation's founding fathers?":
            show jack neutral:
                zoom 2.0 yalign 0.1 xalign 2.0 rotate 30
            j "{b}No.{/b}"
            show jack neutral:
                zoom 1.0 yalign 0.0 xalign 0.5 rotate 0

        "Would you accept a Hamburger I have had in my pocket since last thursday?":
            j "I don't even want to know why you keep hamburgers in your pocket... especially for that long!"
    jump post_tour_lobby

label post_tour_lobby:
    scene lobby
    show jack neutral
    j "Anyways, I believe that concludes our tour"
    j "Before you start working here, employee, I have to ask you a few questions"

    $ player_name = renpy.input("What is your name?")

    $ player_name = player_name.strip()

    if player_name == "":
        $ player_name = "Employee"

    j "Ok, good"
    j "Now, have you committed any crimes, eco-terrorism, and/or contracted the Bubonic plague ever in your life?"
    $ does_jack_want_to_touch_you = 0
    menu:
        j "Now, have you committed any crimes, eco-terrorism, and/or contracted the Bubonic plague ever in your life?"

        "I am the sole party responsible for 9/11, and I piloted both the planes":
            j "Oh, so nothing serious then"

        "I have rabies.":
            j "{i}Just stay 6 feet away from me and all the customers, and you should be fine{/i}"

        "I'm a drama kid":
            j "{i}I'm putting you on a watchlist.{/i}"

        "I'm the guy who puts anime stickers on his car":
            j "{i}Please don't touch me ever again{/i}"
            $ does_jack_want_to_touch_you += 1

        "I burn orphanages in my spare time":
            j "They were taking up tax dollars anyway"

    j "Ok, all seems to be good"
    if does_jack_want_to_touch_you == 1:
        "{i}He cautiously shakes your hand and then wipes it on the cuff of his pants like you're diseased{/i}"
    if does_jack_want_to_touch_you == 0:
        "{i}He shakes your hand{/i}"
    jump lobby

return
