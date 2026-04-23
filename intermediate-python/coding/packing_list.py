import csv

data = [["Item", "Quantity"], ["Blender", 2], ["Posters", 30], ["Shoes", 2]]

packing_list_file_path = "packing_list.csv"

# Forma Manual de Cerrar el Archivo

# try:
#     file = open(packing_list_file_path, "r", encoding="utf8")
#     csv_reader = csv.reader(file)
#     for row in csv_reader:
#         print(row)
# except FileNotFoundError:
#     print("Packing list file not found. Creating a new one.")
#     file = open(packing_list_file_path, "w", newline="")
#     csv_writer = csv.writer(file)
#     csv_writer.writerows(data)
# finally:
#     file.close()

# Forma recomendada

try:
    with open(packing_list_file_path, "r", encoding="utf8") as file:
        csv_reader = csv.reader(file)
        for row in csv_reader:
            print(row)
except FileNotFoundError:
    print("Packing list file not found. Creating a new one.")
    with open(packing_list_file_path, "w", newline="") as file:
        csv_writer = csv.writer(file)
        csv_writer.writerows(data)
