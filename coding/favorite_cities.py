class City:
    def __init__(self, name, country, population, landmarks, founding_year, mayor):
        self.name = name
        self.country = country
        self.population = population
        self.landmarks = landmarks
        self.founding_year = founding_year
        self.mayor = mayor


buenos_aires = City("Buenos Aires", "Argentina", 14000000, ['Obelisco', 'Casa Rosada', 'Estadio Alberto J. Armando'], '1820', 'Axel Kicillof')
tokyo = City("Tokyo", "Japan", 41000000, ['Tokyo Tower', 'Senso-ji Temple', 'Shibuya Crossing'], '1457', 'Yuriko Koike')

print(vars(buenos_aires))
print(vars(tokyo))