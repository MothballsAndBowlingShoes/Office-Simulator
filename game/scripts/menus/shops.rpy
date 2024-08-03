#
# shops.rpy
# OfficeSimulator
#
# Created by Atticus Young on 7/10/24.
# 
# 

# MARK: shops entry point
init python:
    class Item:
        def __init__(self, name, cost):
            self.name = name
            self.cost = cost

    class Inventory:
        def __init__(self, money = 25):
            self.money = money
            self.items = []

        def buy(self, item):
            if self.money >= item.cost:
                self.money -= item.cost
                self.items.append(item)
                return True
            else:
                return False

        def addMoney(self, amount):
            self.money += amount

        def has_item(self, item):
                if item in self.items:
                    return True
                else:
                    return False

label hallway_vendingMachineMenu_vendingMachineShops:
    python:
        inventory = Inventory()
        
        #Items
        BritishTea = Item("British Tea", 25)
    
    "What would you like to buy, sweetcheeks?"

    menu shop:
        "What would you like to buy, sweetcheeks?"
        
        "Buy BritishTea: [BritishTea.cost]$":
            if inventory.buy(BritishTea):
                "You buy the British Tea"
                jump shop
            else:
                v "Sorry Hot Stuff, you don't have enough. Come back with something {b}bigger{/b}~"
                jump hallway_vendingMachineMenu_vendingMachineShops
        
        "Return":
            jump vallory
