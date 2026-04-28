# Encontrá todas las ocurrencias de la palabra "midu" en el siguiente texto, indicá en qué posición empieza y termina cada una, y cuántas veces se encontró: `"Este es el curso de Python de midudev. ¡Suscríbete a midudev si te gusta este contenido! midu"`

import re as rgx

text = "Este es el curso de Python de midudev. ¡Suscríbete a midudev si te gusta este contenido! midu"
pattern = "midu"

result = rgx.finditer(pattern, text)

for match in result:
    print(match.group(), match.start(), match.end())
