label bathroom:  # Defining a label called 'bathroom'
    scene bathroom  # Displaying the bathroom scene

    "You enter the dank and moldy bathroom"

    if bonzi_quest_stage == 0:  # Checking if the variable 'first_visit' is equal to 0
        jump bonzi_intro  # Jumping to the label 'bonzi_intro' if the condition is true
        bonzi_quest_stage += 1
    elif bonzi_quest_stage == 0 && bonzi_quest_update == true:
        jump bonzi_quest0
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