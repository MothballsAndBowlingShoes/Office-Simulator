# 
# randy.rpy
# Office-Simulator
#
# Created by Atticus Young on 8/2/24.
# 
# 

# MARK: randy entry point
label randy:
    scene bg cubicle
    show randy neutral
    
    r "Hey %(player_name)s"
    
    menu:
        "Talk to Randy.":
            r "Yep, you're talking too me all right"
            jump randy
        
        "Go Back":
            jump offices
    
    return
