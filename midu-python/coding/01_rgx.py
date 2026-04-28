# Encontrá la primera ocurrencia de la palabra "IA" en el siguiente texto e indicá en qué posición empieza y termina: `"Todo el mundo dice que la IA nos va a quitar el trabajo. Pero solo hace falta ver cómo la puede cagar con las Regex para ir con cuidado"`

import re as rgx

text = "Todo el mundo dice que la IA nos va a quitar el trabajo. Pero solo hace falta ver cómo la puede cagar con las Regex para ir con cuidado"
pattern = "IA"

result = rgx.search(pattern, text)

if result:
    print(result.group())  # pyright: ignore[reportOptionalMemberAccess]
    print(result.start())
    print(result.end())
