# 
# giuseppe.rpy
# Office-Simulator
#
# Created by Atticus Young on 8/5/24.
# 
# 

# MARK: giuseppe entry point

########################################################################################
## Variables
########################################################################################
default metGiuseppe = False

########################################################################################
## Labels
########################################################################################
## giuseppe ############################################################################
##
## This code defines the giuseppe label.
label giuseppe:
    if metGiuseppe == False:
        # music here
        show giuseppe neutral
        with fade
        g "Psttt..."
        n "You hear a whisper."
        g "Psttt... you'rrre de new employee, %(player_name)s, rrright-a?"
        n "The italian shakes his hand."
        menu:
            "WOAH! Are you a {i}real{/i} italian man?":
                g "No! In fact-a, I am-a..."
                
            "Out of my way Pasta-Man, I have Salad Bars to fuck.":
                g "Wait-a, give me a second-a!"
        
        # Change track here w/ Fade
        show white
        with dissolve
        pause 0.5
        hide white
        with dissolve
        play sound giuseppeMustacheRemove
        show giuseppe neutralnostache
        ci "I am actually detective Cast Iron!"
        ci "I am a secret agent for the Tennessee Valley Authority!"
        ci "I would like your help with my task."
        ci "You see, the company has been embezelling funds and avoiding paying it's taxes, {i}among other work place violations{/i}."
        ci "I need a fresh face to help me arrest and bring the other employees to Justice."
        menu:
            "Hmmm... What's in it for me?":
                ci "Well, for one you get to fuck others over, while also doing the right thing."
                g "But we'll also pay you handsomely for your work and scrub your criminal record clean of all your crimes against humanity. {size=-8}{i}{w}We know about what happened with the Vegas Stripper church.{/i}{/size}"
                
        "There's no need to decide now, but if you decide you want to help me, you know where to find me"
    
    $ metGiuseppe = True
    hide giuseppe
    with fade
    return
