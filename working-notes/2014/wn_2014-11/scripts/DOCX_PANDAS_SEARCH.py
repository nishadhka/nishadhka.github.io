import csv
import pandas as pd

#to remove empty line in csv file
input = open('CBE_North_ind.csv', 'rb')
output = open('CBEN2.csv', 'wb')
writer = csv.writer(output)
for row in csv.reader(input):
    if any(field.strip(']') for field in row):
        writer.writerow(row)
input.close()
output.close()
db=pd.read_csv('CBEN2.csv',delimiter=']')
db
da=pd.isnull(db['Products manufactured with Quantity and Intermediate / By-Products manufactured with Quantity'])
db['Nullys']=pd.isnull(db['Products manufactured with Quantity and Intermediate / By-Products manufactured with Quantity'])
rec=db.sort(['Nullys'],ascending=[1])
rec=db.sort(['Nullys'],ascending=[0])
rec.head()
db=pd.read_csv('CBE_North_ind.csv',delimiter=']')
db1=db[db['Name and Factory address'].str.contains("Annur")]
db2=db[db['Category-Classification Type GFA BS or AC submitted/as on'].str.contains("Red-Large")]
db2=db[db['Category-Classification Type GFA BS or AC submitted/as on'].str.contains("Red-Medium")]
db2=db[db['Category-Classification Type GFA BS or AC submitted/as on'].str.contains("Red-Large")]
db2=db[db['Category-Classification Type GFA BS or AC submitted/as on'].str.contains("process involving foundry ")]
db2=db[db['Category-Classification Type GFA BS or AC submitted/as on'].str.contains("foundry")]
db2=db[db['Category-Classification Type GFA BS or AC submitted/as on'].str.contains("-Hotels ")]
db2=db[db['Category-Classification Type GFA BS or AC submitted/as on'].str.contains("Industry")]
