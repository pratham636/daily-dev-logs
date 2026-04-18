import pandas as pd
df=pd.read_csv('pokemon_data.csv')
# df.to_csv('modified.csv',index=False)  # Make new file 
                                         # If you not want to enter index write false
# df.to_excel('modified2.xlsx',index=False)
df.to_csv('modified.txt',index=False)
