import numpy as np
import pandas as pd
import csv

csv_path = 'C:\\Users\\16306\Documents\\UIUC OMCS\\CS 498 - Data Visualization\\7-3-3\pokemon.csv'
pk = pd.read_csv(csv_path)

counter = pd.DataFrame(data=np.zeros((7,18)),columns=['normal', 'fire', 'fighting', 'water', 'flying', 'grass', 'poison', 'electric', 'ground', 'psychic', 'rock', 'ice', 'bug', 'dragon', 'ghost', 'dark', 'steel', 'fairy'])
types = ['normal', 'fire', 'fighting', 'water', 'flying', 'grass', 'poison', 'electric', 'ground', 'psychic', 'rock', 'ice', 'bug', 'dragon', 'ghost', 'dark', 'steel', 'fairy']

for i in range(0, pk.shape[0]):
    gen = pk.iloc[i].loc['generation']
    t1 = pk.iloc[i].loc['type1']
    t2 = pk.iloc[i].loc['type2']
    
    if not pd.isnull(t1):
        counter.iloc[gen-1].loc[t1] += 1
    if not pd.isnull(t2):
        counter.iloc[gen-1].loc[t2] += 1
        
print(counter)
counter.to_csv('Type Dist by Gen.csv')