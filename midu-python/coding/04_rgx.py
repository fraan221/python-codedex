# Validá que un correo electrónico pertenezca a Gmail: `"miduga@hotmail.com"`

import re as rgx

email = "miduga@hotmail.com"
pattern = r"@gmail\.com$"

valid = rgx.search(pattern, email)
if valid:
    print("Email match.")
else:
    print("Email not match.")
