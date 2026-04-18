import pandas as pd
df=pd.read_csv('pokemon_data.csv')
# df=pd.read_excel('pokemon_data.xlsx')
# print(df)             #Print all data
print(df.head(3))       #Print top 3 data
print(df.tail(3))       #Print bottem 3 data

tdf=pd.read_csv('pokemon_data.txt',delimiter='\t') #for txt file we add delimiter
print(tdf)