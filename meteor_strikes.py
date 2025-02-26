import pandas as pd

db = pd.read_csv('Meteorite_Landings.csv')
for num in range(len(db['reclat'].head(5))):
    print(db['reclat'][num], db['reclong'][num])