class CoffeeMenu:
    def __init__(self):
        self.menu = {
            "espresso": 2.50,
            "latte": 2.75,
            "cappuccino": 3.20,
            "americano": 2.70,
        }

    def get_price(self, item):
        return self.menu.get(item.lower())

    def modify_price(self, key, value):
        if key in self.menu:
            return self.menu.update({key: value})

    def add_item(self, key, value):
        return self.menu.update({key: value})

    def delete_item(self, key):
        return self.menu.pop(key)


m = CoffeeMenu()
