from csvpart import darbas,darbas2
import csv
file = open('source.csv')
csv_reader = csv.DictReader(file)
rows=[]
for row in csv_reader:
    if row['countryterritoryCode'] not in rows:
        rows.append(row['countryterritoryCode'])
        rows.append(row['countriesAndTerritories'])
print(rows)
print(csv_reader)
print("iveskite šalies koda")
country=input()
d1 = darbas(country,'source.csv')
d1.function()
print("iveskite menesi")
month = input()
d2 = darbas2(month,'source.csv')
d2.func()