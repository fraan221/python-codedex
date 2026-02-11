earth_weight = float(input("Earth Weight: "))
planet_number = int(input("Planet number: "))

mercury_relative = 0.38
venus_relative = 0.91
mars_relative = 0.38
jupiter_relative = 2.53
saturn_relative = 1.07
uranus_relative = 0.89
neptune_relative = 1.14

if planet_number == 1:
    destination_weight = earth_weight * mercury_relative
    print("Mercury weight: " + str(destination_weight))
elif planet_number == 2:
    destination_weight = earth_weight * venus_relative
    print("Venus weight: " + str(destination_weight))
elif planet_number == 3:
    destination_weight = earth_weight * mars_relative
    print("Mars weight: " + str(destination_weight))
elif planet_number == 4:
    destination_weight = earth_weight * jupiter_relative
    print("Jupiter weight: " + str(destination_weight))
elif planet_number == 5:
    destination_weight = earth_weight * saturn_relative
    print("Saturn weight: " + str(destination_weight))
elif planet_number == 6:
    destination_weight = earth_weight * uranus_relative
    print("Uranus weight: " + str(destination_weight))
elif planet_number == 7:
    destination_weight = earth_weight * neptune_relative
    print("Neptune weight: " + str(destination_weight))
else:
    print("Invalid planet number")
