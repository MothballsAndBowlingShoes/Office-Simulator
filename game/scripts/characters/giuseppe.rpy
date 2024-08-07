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
        play music giuseppeTheme fadeout 1.0 fadein 1.0
        show giuseppe neutral
        with fade
        g "Psttt..."
        n "You hear a whisper."
        g "Psttt... you'rrre de new employee, %(player_name)s, rrright-a?"
        n "Before you is a clearly very real italian man and not at all a very poor sterotype."
        menu:
            "WOAH! Are you a {i}real{/i} italian man?":
                g "No! In fact-a, I am-a..."
                
            "Out of my way Pasta-Man, I have Salad Bars to fuck.":
                g "Wait-a, give me a second-a!"
        
        show white
        with dissolve
        pause 1
        show giuseppe neutralnostache
        play sound giuseppeMustacheRemove
        hide white
        with dissolve
        play music castIronTheme fadeout 1.0 fadein 1.0
        ci "I am actually world famous detective, Officer Cast Iron!"
        ci "I am a secret agent for the Tennessee Valley Authority!"
        ci "I would like your help with my task."
        ci "You see, the company has been embezelling funds and avoiding paying it's taxes, {i}among other work place violations{/i}."
        ci "I need a fresh face to help me arrest and bring the other employees to Justice."
        menu:
            "Hmmm... What's in it for me?":
                ci "Well, for one you get to fuck others over, while also doing the right thing."
                ci "But we'll also pay you handsomely for your work and scrub your criminal record clean of all your crimes against humanity. {size=-8}{i}{w}We know about what happened with the Vegas Stripper church.{/i}{/size}"
            "Do I get to be a Detective too?":
                ci "Do well enough we'll see, right now though you'll only be probationary."
        
        
        menu:
            "I'm not sure...":
                ci "There's no need to decide now, but if you decide you want to help me, you know where to find me. Take some time to think about it."
                
            "Count me in.":
                ci "Welcome aboard, %(player_name)s."
                ci "Come back to me when you're read for your first assignment."
                $ giuseppeQuest.currentQuestStage = 10
                $ questLog.append(giuseppeQuest)
        $ metGiuseppe = True
        hide giuseppe
        with fade
    if giuseppeQuest.currentQuestStage == 10:
        g "I take it you're ready for your first assignment?"
    return
