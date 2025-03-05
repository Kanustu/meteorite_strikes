import pandas as pd

db = pd.read_csv('Meteorite_Landings.csv')
meteor_lat = []
meteor_long = []
for num in range(len(db['reclat'].head(5))):
    meteor_lat.append(db['reclat'][num])
    meteor_long.append(db['reclong'][num])
print(meteor_lat[0], meteor_long[0])