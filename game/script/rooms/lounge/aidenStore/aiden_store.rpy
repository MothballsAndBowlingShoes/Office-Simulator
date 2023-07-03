# Define the player's initial money
$ init_money = 100

# Shop inventory dictionary
$ shop_inventory = {
    "item1": {"name": "Item 1", "price": 10},
    "item2": {"name": "Item 2", "price": 20},
    "item3": {"name": "Item 3", "price": 30}
}

# Initialize the player's money
$ money = init_money

# Shop interface
label shop:
    $ selected_item = None
    screen shop():
        frame:
            vbox:
                hbox:
                    text "Money: $[money]"

                vbox:
                    for item_key, item in shop_inventory.items():
                        hbox:
                            text "[item['name']] - $[item['price']]"
                            textbutton "Buy" action [buy_item(item_key)]
                hbox:
                    textbutton "Exit" action [Return()]

# Function to buy an item from the shop

label buy_item(item_key):
    $ selected_item = item_key

    if item_key in shop_inventory:
        $ item = shop_inventory[item_key]
        if money >= item["price"]:
            $ money -= item["price"]
            # Add code here to handle the purchase logic
            # For example, adding the item to the player's inventory
            # or updating some game variables.
            return
    # If the purchase is not successful, display a message
    $ selected_item = None
    "You don't have enough money to buy this item."
