#
# script.rpy
# OfficeSimulator
#
# Created by Atticus Young on 2/21/24.
#
#

# MARK: script entry point

default inventory = [employeeID, deadRat]

label start:
    show screen timeAndDay
    #call tour
    jump lobby
return
