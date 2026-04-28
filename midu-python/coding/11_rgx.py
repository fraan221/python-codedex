# Igual que el anterior pero ahora con coincidencias parciales en el medio — encontrá solo las palabras exactas man, fan y ban: "omniman fanatico man bandana"

import re as rgx

text = "omniman fanatico man bandana"
pattern = r"\b[mfb]an\b"

matches = rgx.findall(pattern, text)

print(matches)
