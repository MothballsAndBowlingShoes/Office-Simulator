label neverEndingHallway:
    scene bg decrepithallway
    play music hallwayAmbience
    
    menu:
        n "What would you like to do?"
        
        "Go further down the hallway.":
            $ jump_random_hallway()
                
        "Go back.":
            jump hallway

label hallway_event_0:
""

# Aiden hallway event
label hallway_event_1:
    play music backroomsAmbience
    scene bg backrooms

    n "You enter a mysterious yellow room..."
    n "You smell the faint smell of Whiskey on the air..."
    
    # Show Aiden's neutral expression and cover him with a image for 8 frames
    # This is used to create a brief animation effect
    show aiden neutral at aiden_peek_1
    show aiden_cover 1
    pause 8

    # Show Aiden's neutral expression and cover him with a image for 8 frames
    # This is used to create a brief animation effect
    show aiden neutral at aiden_peek_2
    show aiden_cover 2
    pause 8

    # Show Aiden's neutral expression and cover him with a image for 10 frames
    # This is used to create a brief animation effect
    show aiden neutral at aiden_peek_3
    show aiden_cover 3

    pause 10
    "He's here..."

    # Resets Aiden's Position
    show aiden neutral at aiden_reset
    with easeinbottom
    pause 0.5
    hide aiden_cover


    a "You should buy stuff from me"
    
    menu:
        "Leave while you still have your kidneys and remain unblinded":
            jump neverEndingHallway

label hallway_event_2:
""

label hallway_event_3:
""

label hallway_event_4:
""

label hallway_event_5:
""

label hallway_event_6:
""

label hallway_event_7:
""

label hallway_event_8:
""

label hallway_event_9:
""
