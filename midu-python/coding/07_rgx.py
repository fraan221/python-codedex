# Hacé opcional que aparezca el prefijo +34 en el siguiente número de teléfono: "+34 688999999"

import re as rgx

phone = "688999999"
pattern = r"(\+34 )?\d{9}"

match = rgx.findall(pattern, phone)

print(match)
