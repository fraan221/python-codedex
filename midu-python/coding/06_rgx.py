# ¿Cuántas palabras tienen de 0 o más "a" seguidas de una "b"?

import re as rgx

text = "ab aab b aaab ba abc"
pattern = r"a*b"

match = rgx.findall(pattern, text)

print(match)
