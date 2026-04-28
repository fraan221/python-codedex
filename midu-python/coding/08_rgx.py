# Encontrá las palabras de entre 4 y 6 letras en el siguiente texto: "ala casa árbol león cinco murcielago"

import re as rgx

text = "ala casa árbol león cinco murcielago"
pattern = r"\b\w{4,6}\b"

matches = rgx.findall(pattern, text)

print(matches)
