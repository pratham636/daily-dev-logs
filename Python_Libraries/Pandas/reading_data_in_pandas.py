import pandas as pd
df=pd.read_csv('pokemon_data.csv')



#Read Headers
# print(df.columns)
#Read each Colums
# print(df['Name'])
# print(df['Name'][0:5])
# print(df.Name)
# print(df[['Name','Type 1','Type 2','HP']])



#Read each Row
# print(df.iloc[3])
# print(df.iloc[1:5])
# Read a specific location (R,C)
# print(df.iloc[2,1])



#loop to get information in each row
# for index,row in df.iterrows():
#     print(index,row)
# for index,row in df.iterrows():
#     print(index,row['Name'])



# Want specific data
print(df.loc[df['Type 1']=="Fire"])



print(df.describe())



