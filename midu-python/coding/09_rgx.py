# Encontrá las palabras de más de 6 letras en el siguiente texto: "ala fantastico casa árbol león cinco murcielago"

import re as rgx

text = "ala fantastico casa árbol león cinco murcielago"
pattern = r"\b\w{6,}\b"

matches = rgx.findall(pattern, text)

print(matches)
