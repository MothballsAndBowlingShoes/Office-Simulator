# 
# jack-quest-intro.rpy
# OfficeSimulator
#
# Created by Atticus Young on 2/17/24.
# 
# 

# MARK: jack-quest entry point
label JackIntro:
    "You aproach Jack, he looks like he's hard at work thinking about something"
    j "Say, employee, you said you've only committed a {i}few{/i} crimes, right?"
    menu:
        j "Say, employee, you said you've only committed a {i}few{/i} crimes, right?"
        
        "Well... The court {i}did{/i} say the Nuking of that Pizza Joint in Canada didn't count due to the pizza being so horrendous it was self defense":
                j "Well, as long as you stay away from the McDonalds down the street we should be fine"
        "Is serial Arsonry considered a Crime?":
            j "Only in California!"
    
    j "Either way i need a favor from you."
    j "You see, i suspect some of our employess to be hampering our... {i}productivity{/i}"
    j "I was hoping you could... take them out"
    
    menu:
        j "I was hoping you could... take them out"
        
        "Are you suggesting I kill them?":
            j "Woah Woah Woaah... don't be so hasty there"
            j "I just want them out of the way"

        "Like on a date? Where we'll go back to their place, then sultrily undress in the candlelight and they will gently stroke my skin and whisper sweet nothings to me. Then they pin me to the bed, moaning my name as we make sweet passionate love to eachother and then they grasp my-":
            show jack neutral:
                zoom 2.0 yalign 0.1 xalign -0.5 rotate -30
            play audio sprayBottle
            show image "sprayBottle.png"
            j "{b}NO EMPLOYEE{/b}"
            
            show jack neutral:
                zoom 1.0 yalign 0.0 xalign 0.5 rotate 0
            hide image "sprayBottle.png"
    j "Look... You can kill them or get them fired, either way i don't care"
    j "just don't make the company look bad"
    j "If you do this I may even reward you..."
    menu:
        j "If you do this I may even reward you..."
        
        "Can I have head scwitches fow a good job mastew uwu":
            #add affect for jack vomitting
            "{i}Jack vomits all over the floor{/i}"
        "I want to fuck the salad bar":
            j "W-Wha-"
            menu:
             "You heard me. I want to rawdog that salad":
                j "Employee please..."
                menu:
                    "I will cummies all over the salad":
                        j "No!"
                        j "Please... i don't want to talk about this anymore... it scares me."
                        j "just... will you do it?"
    menu:
        "Fine... but I expect to have full Salad Fucking Privileges":
            j "{b}Out of my office{/b}"
        "Yes":
            j "Good, now go"
        "Yes (But lying)":
            j "Good, now go"
            
