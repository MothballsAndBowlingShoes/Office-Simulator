init python:
    class item:
        value = 0
        name = "null"
        def __init__(self, name, value):
            self.item = "Item"
            self.name = name
            self.value = value

    class trait:

        name = "null"
        playerHave = True
        def __init__(self, name, playerHave):
            self.item = "Item"
            self.name = name
            self.playerHave = playerHave


    
$ persistent.playerTraits = []
$ persistent.inventory = []
$ persistent.officeCoinAmount = 0
$ persistent.sherylPoints = 0
