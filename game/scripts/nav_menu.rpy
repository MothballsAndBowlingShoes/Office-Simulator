# 
# nav_menu.rpy
# OfficeSimulator
#
# Created by Atticus Young on 7/14/24.
# 
# 

# MARK: nav_menu entry point
#style nav_button:
    
screen nav_menu(lst):
    style_prefix "choice"
    vbox:
        for i in lst:
            textbutton i:
                if i=="Nevermind":
                    action Return()
                else:
                    action Jump(i.lower())


