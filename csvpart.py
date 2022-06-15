import csv
import datetime
import pandas as pd
import json
import os
class darbas:
    def __init__(self, country,source):
        self.country = country
        self.source=source
    def function(self):
        file = open(self.source)
        csv_reader = csv.DictReader(file)
        y = datetime.datetime.now().strftime('%Y-%m-%d')
        z = datetime.datetime.now().strftime('%H_%M_%S')
        f = open('generated/generated'+'_'+y+'_'+z+'.csv', 'w', newline='')
        writer = csv.writer(f)
        writer.writerow(['countryterritoryCode', 'countriesAndTerritories', 'dateRep', 'cases', 'deaths'])
       
        for row in csv_reader:
            ctcode=row['countryterritoryCode']
            ct=row['countriesAndTerritories']
            d=datetime.datetime.strptime(row['dateRep'], '%d/%m/%Y').strftime('%Y-%m-%d')
            cases=row['cases']
            deaths=row['deaths']
            if row['countryterritoryCode']==self.country: 
                writer.writerow([ctcode,ct,d,cases,deaths])
class darbas2:
    def __init__(self,month,source):
        self.source = source
        self.month = month
    def func(self):
        df = pd.read_csv(self.source, sep=',')
        y = datetime.datetime.now().strftime('%Y-%m-%d')
        z = datetime.datetime.now().strftime('%H_%M_%S')

        df2=df.groupby(['countryterritoryCode','countriesAndTerritories','year','month'])['cases','deaths'].sum().sort_values(by=["countriesAndTerritories"], ascending=True)

        df2.to_csv ('failas1.csv')


        jsonArray = []  
 
        with open('failas1.csv', encoding='utf-8') as csvf: 
                csvReader = csv.DictReader(csvf) 
                for row in csvReader: 
                    row['cases']=int(row['cases'])
                    row['deaths']=int(row['deaths'])
                    if row['month']==self.month:
                        jsonArray.append(row)
        Dict = {'records':jsonArray}
        os.remove("failas1.csv")
        with open('generated/generated'+'_'+y+'_'+z+'.json', 'w', encoding='utf-8') as jsonf: 
                jsonString = json.dumps(Dict, indent=4)
                jsonf.write(jsonString)
