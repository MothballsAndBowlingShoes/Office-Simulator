# 
# shop.rpy
# OfficeSimulator
#
# Created by Atticus Young on 4/15/24.
# 
# 

# MARK: shop entry point
screen shop():
    modal True
    window id "shop":
        vbox:
            textbutton "British Tea" action [Jump("hallway_vendingMachine")]
