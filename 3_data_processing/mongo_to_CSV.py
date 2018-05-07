#This script is used to parse Route User Star data from the mongo database containg route descriptions
import sys,csv
sys.path.insert(0, '/Users/colinbrochard/DSI_Capstone_local/MtProjRec/1_data_coll/')
import pandas as pd
import mt_scrape_helpers as mh
from pymongo import MongoClient

client = MongoClient()
db = client.routes_db
df = pd.DataFrame(list(db.routes_db.find()))

data = []
for row in df.iterrows():
    parsed = mh.parse_stats(dict(row[1]))
    data += parsed

with open('/Users/colinbrochard/DSI_Capstone_local/MtProjRec/2_data/rus1.csv','w') as out:
    csv_out=csv.writer(out)
    csv_out.writerow(['route','user','num_stars'])
    for row in data:
        csv_out.writerow(row)
