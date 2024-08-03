label jackOffice:
    stop music
    scene bg jackoffice
    n "You enter the Uncomfortably lavish Office"
    n "Jack is standing in the corner, his chair perfectly untouched"
    menu:
        "What do you want to do?"
        
        "Talk to Jack":
            jump JackIntro
            
        "Go back":
            jump hallway
