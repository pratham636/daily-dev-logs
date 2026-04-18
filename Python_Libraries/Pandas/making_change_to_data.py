import pandas as pd
df=pd.read_csv('pokemon_data.csv')
# df['Total'] = df['HP'] + df['Attack'] + df['Defense'] + df['Sp. Atk'] + df['Sp. Def'] + df['Speed'] #Enter new columns
# print(df.head(5))


# df=df.drop(columns=['Total'])   #drop total


df['Total']=df.iloc[:,4:10].sum(axis=1)  

#rearranging columns
# df=df[['Total','HP','Defense']]

cols=list(df.columns.values)
df=df[cols[0:4] + [cols[-1]] + cols[4:12]]

print(df.head(5))
