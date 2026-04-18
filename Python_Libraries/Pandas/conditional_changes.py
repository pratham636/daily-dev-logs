import pandas as pd
df=pd.read_csv('pokemon_data.csv')
# df.loc[df['Type 1']=='Fire','Type 1']='Flamer'             # Change Fire to Flamer

# df.loc[df['Type 1']=='Fire','Legendary']=True                #All fire pokemon are legendary

df['Total'] = df['HP'] + df['Attack'] + df['Defense'] + df['Sp. Atk'] + df['Sp. Def'] + df['Speed']
df.loc[df['Total'] > 500, ['Generation','Legendary']] = 'TEST VALUE'   #greater then 500 so print generation and leagendary to test value
df.loc[df['Total'] > 500, ['Generation','Legendary']] = ['Test 1','Test 2']
print(df)