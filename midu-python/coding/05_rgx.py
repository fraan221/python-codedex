# Dada una cadena con nombres de archivos, encontrá los nombres de los ficheros con extensión .txt: "file1.txt file2.pdf midu-of.webp secret.txt"

import re as rgx

file_names = "file1.txt file2.pdf midu-of.webp secret.txt"
pattern = r"\.txt"

names_valid = rgx.findall(pattern, file_names)

print(names_valid)
