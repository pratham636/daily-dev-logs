import pandas as pd
df=pd.read_csv('modified.csv')
print(df)
# print(df.groupby(['Type 1']).mean())   #Average of type 1 pockmon
# print(df.groupby(['Type 1']).mean().sort_values('Defense',ascending=False))   #Average of type 1 pockmon sorting in deascending
# print(df.groupby(['Type 1']).sum())  #Sum of values

# print(df.groupby(['Type 1']).count()) #count all type pokemon


df['count']=1
# print(df.groupby(['Type 1']).count()['count']) #count all type 1 pokemon in one value count
print(df.groupby(['Type 1','Type 2']).count()['count']) #count all type 2 in type 1 pokemon in one value count