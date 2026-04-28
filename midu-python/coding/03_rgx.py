# Encontrá todas las ocurrencias de la palabra "python" en el siguiente texto sin distinguir entre mayúsculas y minúsculas: `"Este es el curso de Python de midudev. ¡Suscríbete a python si te gusta este contenido! PYTHON"`

import re as rgx

text = "Este es el curso de Python de midudev. ¡Suscríbete a python si te gusta este contenido! PYTHON"

matches = rgx.findall("Python", text, rgx.IGNORECASE)
print(matches)
