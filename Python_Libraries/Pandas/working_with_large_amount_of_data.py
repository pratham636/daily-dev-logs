import pandas as pd
df=pd.read_csv('pokemon_data.csv')
new_df=pd.DataFrame(columns=df.columns)
for df in pd.read_csv('modified.csv',chunksize=5): #data frean but in chunk of file 
    # print("Chunk Df")
    # print(df)
    result=df.groupby(['Type 1']).mean()            #Get a mean of 5 data and condine
    new_df=pd.concat([new_df,result])               #add concat of prevese data and new value
    print(new_df)