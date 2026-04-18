import pandas as pd
df=pd.read_csv('pokemon_data.csv')
# print(df.loc[(df['Type 1']=='Grass') & (df['Type 2']=='Poison')])
# ndf=df.loc[((df['Type 1']=='Grass') | (df['Type 2']=='Poison'))&(df['HP']>70)]



# ndf=ndf.reset_index(drop=True)  #reset index of data
                                #if you want to drop the index
# ndf.reset_index(drop=True,inplace=True)  #same as upside
# print(ndf)
# print(df)



# df=df.loc[df['Name'].str.contains('Mega')]   #get name of mega version
# df=df.loc[~df['Name'].str.contains('Mega')]   #get name of not mega version

# df=df.loc[df['Type 1'].str.contains('Fire|Grass',regex=True)]      #Contain fire or grass 
                                                                     #Regex means or
# df=df.loc[df['Type 1'].str.contains('fire|grass', flags=re.IGNORECASE , regex=True)]
df=df.loc[df['Name'].str.contains('^Pi[a-z]*', regex=True)]
print(df)

