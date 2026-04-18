import pandas as pd
df=pd.read_csv('pokemon_data.csv')

print(df.describe())
# print(df.sort_values('Name'))                           #Assending order
# print(df.sort_values('Name',ascending=False))           #Deassending order

# print(df.sort_values(['Type 1','HP']))
print(df.sort_values(['Type 1','HP'],ascending=[1,0])) #1 assending and 0 dessending