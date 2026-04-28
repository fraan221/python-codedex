# Dado el siguiente texto, encontrá únicamente las palabras man, fan y ban, ignorando el resto: "man ran fan ñan ban"

import re as rgx

text = "man ran fan ñan ban"
pattern = r"[mfb]an"

matches = rgx.findall(pattern, text)

print(matches)
