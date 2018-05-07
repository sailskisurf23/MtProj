import pymongo, csv
import pandas as pd
import numpy as np
from pymongo import MongoClient
client = MongoClient()

grade_map_path = '/Users/colinbrochard/DSI_Capstone_local/MtProjRec/6_app/grade_map.csv'
grade_num_map_path = '/Users/colinbrochard/DSI_Capstone_local/MtProjRec/6_app/grade_num_map.csv'
write_loc = '/Users/colinbrochard/DSI_Capstone_local/MtProjRec/2_data/5_route_features/routes_features.csv'

# pull data from Mongo DB into pd DF
db = client.routesAPI_db
df = pd.DataFrame(list(db.routesAPI_db.find()))

# clean up ratings
with open(grade_map_path) as f:
    data = [line.strip().split("|") for line in f.readlines()]
grade_map = {d[0]: d[1] for d in data}
df['rating0'] = df['rating'].map(grade_map)

# map ratings to number
with open(grade_num_map_path) as f:
    data = [line.strip().split("|") for line in f.readlines()]
grade_num_map = {d[0]: d[1] for d in data}
df['rating_num0'] = df['rating0'].map(grade_num_map)

# grab just the state from location list
df['location0'] = df['location'].apply(lambda x: x[0])

# map route types to simplified categories
conditions_t = [
    (df['type'] == 'Sport') | (df['type'] == 'Sport, Aid'),
    (df['type'] == 'Boulder'),
    (df['type'] == 'Trad')]
choices_t = ['Sport', 'Boulder', 'Trad']
df['type0'] = np.select(conditions_t, choices_t, default='Trad')

# bucket routes into single or multipitch, based on number of pitches
conditions_p = [(df['pitches'] == 1) | (df['pitches'] == '')]
choices_p = ['single-pitch']
df['pitches0'] = np.select(conditions_p, choices_p, default='multi-pitch')

#reorder columns, drop duplicates and write to csv
df_features = df[['id','name','type0','rating0','rating_num0','pitches0','location0']]
df_features.drop_duplicates(inplace=True)
df_features.to_csv(write_loc, sep='|')
