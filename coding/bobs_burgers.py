from coding.restaurants import Restaurants

bobs_burgers = Restaurants()

bobs_burgers.name = 'Bob\'s Burgers'
bobs_burgers.category = 'American Diner'
bobs_burgers.rating = 4.7
bobs_burgers.delivery = False

daleo = Restaurants()

daleo.name = "Da Leo"
daleo.category = "Pizzeria"
daleo.rating = 4.5
daleo.delivery = True

el_antojo = Restaurants()

el_antojo.name = "El Antojo"
el_antojo.category = "Bodegon"
el_antojo.rating = 4.8
el_antojo.delivery = True

print(vars(bobs_burgers))
print(vars(daleo))
print(vars(el_antojo))