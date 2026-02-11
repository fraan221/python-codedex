pesos_colombianos = int(input("What do you have left in pesos? "))
soles_peruanos = int(input("What do you have left in soles? "))
reais_brasilenos = int(input("What do you have left in reais? "))

pesos_colombianos_to_usd = pesos_colombianos * 0.00027
soles_peruanos_to_usd = soles_peruanos * 0.30
reais_brasilenos_to_usd = reais_brasilenos * 0.19

total_usd = pesos_colombianos_to_usd + soles_peruanos_to_usd + reais_brasilenos_to_usd

print(total_usd)
