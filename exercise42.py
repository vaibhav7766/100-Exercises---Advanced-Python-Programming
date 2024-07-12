import csv

with open("Customer.csv", "r", encoding="utf-8") as f:
    reader = csv.reader(f)
    columns = next(reader)
    rows = [row for row in reader]
    country_idx = columns.index("Country")
    countries = [row[country_idx] for row in rows]


def remove_duplicates(n, arr):
    clean = []
    for i in range(n - 1):
        if arr[i] != arr[i + 1]:
            clean.append(arr[i])
    return clean


countries = sorted(countries)
unique_countries = remove_duplicates(len(countries), countries)
print(unique_countries)
