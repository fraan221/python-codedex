import csv

csv_file_path = "/home/fraan/Documents/Study/python/codedex/intermediate-python/coding/Bestseller - Sheet1.csv"

best_selling_book = None
max_sales = 0

with open(
    csv_file_path,
    "r",
    encoding="utf8",
) as csv_file:
    csv_reader = csv.reader(csv_file)
    csv_file.readline()
    for row in csv_reader:
        current_sales = float(row[4])

        if current_sales > max_sales:
            max_sales = current_sales
            best_selling_book = row

output_file_path = "bestseller_info.csv"
with open(output_file_path, "w", newline="") as output_file:
    csv_writer = csv.writer(output_file)
    csv_writer.writerow(["Book", "Author", "Sales in Millions"])
    csv_writer.writerow(
        [best_selling_book[0], best_selling_book[1], best_selling_book[4]]
    )
