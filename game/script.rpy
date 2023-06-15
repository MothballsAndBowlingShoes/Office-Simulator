init:

    python:

        import math

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
                self.start = [ self.anchors.get(i, i) for I in start ]  # central position
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
    #

init:
    $ sshake = Shake((0, 0, 0, 0), 1.0, dist=15)

define j = Character("Jack", what_slow_cps=50, what_slow_abortable=False, color="#ffffff")
#define d = Character("Great Dark One")
define y = Character("You", what_slow_cps=50, what_slow_abortable=False, color="#ffffff")
define a = Character("Aiden", what_slow_cps=50, what_slow_abortable=False, color="#ffffff")
define b = Character("Bonzi", what_slow_cps=50, what_slow_abortable=False, color="#ffffff")

label start:
    scene lobby
    play music "main.mp3"
    show jack_neutral
    j "Welcome to your {i}new{/i} and {i}mostly{/i} unpaid and illegal job"
    menu:
        "isn't their a process to these things?":
            j "No"
            j "Your hired"
            j "No questions asked"
    j "I'm the staff manager, jack"
    j "We have been short on staff ever since everyone else was blinded by Aidens reflective irish skin, so it's a miracle you came when you did."
    menu:
        "Is your head a microwave?":
            j "Yes"
            j "My father was a Parasonic HomeCook MM-GN08KP"
            j "He was one of the few microwaves I was proud to know"
            j "He libertated the country of texas from it's tyrnnical communist oppresors and ushered in an age of capitlist utopia"

            menu:
                "what about your mother?":
                    j "EMPLOYEE, WE DO NOT TALK ABOUT MY DIRTY COMMUNIST MOTHER, DO YOU UNDERSTAND ME?"
                    menu:
                        "Yes sir...":
                            "the man with a microwave for a head shakes it in disapointment"
                            jump tour_lobby


        "wait, blinded?":
            j "who said anything about blinded?"
            y "you di-"
            jump tour_lobby
label tour_lobby:
    j "anyways, let me give you the tour"
    j "this here is the lobby"
    j "This where we put up our corprate front to throw the unsuspecting federal agents off our trail"
    j "if you listen closely, you can hear their screams from the {b}pit{/b}"
    jump tour_elevator

label tour_elevator:
    scene elevator
    with fade
    show jack_neutral
    play music "e1.ogg"
    j "this here is the elevator, your local hub for navigating around the building"
    j "{i}ignore the smell of sweat & dried blood, we still haven't cleaned up after the janitorial department's unsupervised orgy last week{/i}"
    j "Also"
    j "If you hear any creaking coming from the shaft, just remember our company motto:"
    show jack_pointing
    j "{i}Your easily expendable and you will be replaced withing the first 10 hours{/i}"
    jump tour_lounge

label tour_lounge:
    scene lounge
    show jack_neutral

    j "this here is the employee lounge"
    j "this is where you can relax after a day of hard work"
    j "it's also where you will sleep"
    j "As if by some video game logic, just laying in one of the beds will skip you ahead to the next day!"

    menu:
        "can't I sleep at home?":
            show jack_neutral
            with Shake((0, 0, 0, 0), 0.5, dist=30)
            j "NO! ONCE YOU ENTER HERE THERE IS NO LEAVING!"
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
            j "You can run down to the local McDonalds or Eat the roaches off the floor, either one works"
            show jack_neutral:
                zoom 2.0 yalign 0.1 xalign -0.5 rotate -30
            j "{i}If I were you I know which one I would choose{/i}"
            show jack_neutral:
                zoom 1.0 yalign 0.0 xalign 0.5 rotate 0
            menu:
                "Can I use your head to cook my food?":
                    j "Please don't"
                    j "last time that happened it took a week to clean all that lasagna"
                    j "{i}I can stil taste Daves pasta sauce{/i}"
                    "{i}He shudders{/i}"
                    jump tour_boardroom



label tour_boardroom:
    scene boardroom
    show jack_neutral
    j "This is the board room!"
    j "Here, we host daily briefings on company updates that range from {i}helpful{/i} to {i}not helpful at all{/i}"
    j "This is also where Aiden sells his goods"
    show jack_neutral:
        ease 1 left
    show aiden:
        right
    with moveinright
    a "Bask in my pale skin in its blinding glory"
    j "{i}try to avoid staring at him for too long...{/i}"
    j "also, anything you hear from police reports about him consuming families is purely rumor and Speculation... \n{i}probably{/i}..."
    hide aiden
    show jack_neutral:
    j "he will sell you objects you might need in exchange for our new crypto currency"
    j "{b}Office Coin{/b}"
    menu:
        "Do you accept the fiscal monetary standard established in 1792 by this fine nations founding fathers?":
            show jack_neutral:
                zoom 2.0 yalign 0.1 xalign -0.5 rotate -30
            j "{b}no.{/b}"
            show jack_neutral:
                zoom 1.0 yalign 0.0 xalign 0.5 rotate 0
    jump post_tour_lobby

label post_tour_lobby:
    scene lobby
    show jack_neutral
    j "anyways, i belive that concludes our tour"
    j "before you start working here employee, i have to ask you a few questions"

    $ player_name = renpy.input("What is your name?")

    $ player_name = player_name.strip()

    if player_name == "":
        $ player_name="Employee"

    j "ok, good"
    j "now have you commited any crimes, eco terrosim, and/or contracted the Bubonic plague ever in your life?"
    $ does_jack_want_to_touch_you = 0
    menu:
        j "now have you commited any crimes, eco terrosim, and/or contracted the Bubonic plague ever in your life?"

        "I am the sole party responsible for 9/11 and i piloted both the planes":
            j "Oh, so nothing serious then"



        "I have rabies.":
            j "{i}just stay 6 feet away from me and all the customers and you should be fine{/i}"

        "I'm a drama kid":
            j "{i}i'm putting you on a watch list.{/i}"

        "I'm the guy who puts anime stickers on his car":
            j "{i}please don't touch me ever again{/i}"
            $ does_jack_want_to_touch_you += 1

        "I burn orphanages in my spare time":
            j "They were taking up tax dollars anyways"

    j "Ok, all seems to be good"
    if does_jack_want_to_touch_you == 1:
        "{i}He cautiously shakes your hand and then wipes it on the cuff of his pants like your diseased{/i}"
    if does_jack_want_to_touch_you == 0:
        "{i}He shakes your hand{/i}"
    jump lobby












    return
