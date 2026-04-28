# Ejercicio final combinando todo lo aprendido: mejorá y corregí la regex de validación de email cubriendo casos borde como "lo.que+sea@shopping.online" y "michael@gov.co.uk"

import re as rgx

edge_case_1 = "lo.que+sea@shopping.online"
edge_case_2 = "michael@gov.co.uk"

# Válidos
edge_case_3 = "user123@sub.domain.com"
edge_case_4 = "name+filter@gmail.com"
edge_case_5 = "first.last@company.co.ar"
edge_case_6 = "user@domain.museum"

# Inválidos
edge_case_7 = "@nodomain.com"
edge_case_8 = "noatsign.com"
edge_case_9 = "user@.com"
edge_case_10 = "user@domain."
edge_case_11 = "user@@domain.com"

pattern = r"[\w._%+-]+@[\w.-]+\.[a-zA-Z]{2,6}"

match_1 = rgx.findall(pattern, edge_case_1)
match_2 = rgx.findall(pattern, edge_case_2)
match_3 = rgx.findall(pattern, edge_case_3)
match_7 = rgx.findall(pattern, edge_case_7)
match_11 = rgx.findall(pattern, edge_case_11)

print(match_1)
print(match_2)
print(match_3)
if match_7:
    print("Email valid")
else:
    print("Email invalid")

if match_11:
    print("Email valid")
else:
    print("Email invalid")
