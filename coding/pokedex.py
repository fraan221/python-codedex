class Pokemon:
    def __init__(self, entry, name, types, description, is_caught, height, weight, region):
        self.entry = entry
        self.name = name
        self.types = types
        self.description = description
        self.is_caught = is_caught
        self.height = height
        self.weight = weight
        self.region = region

    def speak(self):
        print(f"{self.name * 2}")

    def display_details(self):
        print(f"Entry number: {self.entry}")
        print(f"Name: {self.name}")

        if len(self.types) == 1:
            print(f"Type: {self.types[0]}")
        else:
            print(f"Type: {self.types[0]} / {self.types[1]}")

        print(f"Description: {self.description}")

        if self.is_caught:
            print(f"{self.name} has been already caught!")
        else:
            print(f"{self.name} hasn't been caught.")

        print(f"Height: {self.height}")
        print(f"Weight: {self.weight} lbs")
        print(f"Region: {self.region}")

blaziken = Pokemon(257, "Blaziken", ["Fire", "Fighting"], "It can jump powerfully enough to clear a 30-story building. It uses flaming punches to incinerate its opponents.", True, "6\' 03\"", 114.6, "Hoenn")
conkeldurr = Pokemon(534, "Conkeldurr", ["Fighting"], "It is thought that Conkeldurr taught humans how to make concrete more than 2,000 years ago.", False, "4\' 07\"", 191.8, "Teselia")
charizard = Pokemon(6, "Charizard", ["Fire", "Flying"], "If Charizard becomes truly angered, the flame at the tip of its tail burns in a light blue shade.", True, "5\' 07\"", 199.5, "Kanto")

blaziken.speak()
conkeldurr.speak()
charizard.speak()
print("---")
blaziken.display_details()
print("---")
conkeldurr.display_details()
print("---")
charizard.display_details()