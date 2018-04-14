import os
import time
import random
import MtProjScrapeHelpers as mh

# import pickle
# import pandas as pd
# from bs4 import BeautifulSoup
# import requests
# import urllib
# import json


#import routeIDs for a handful of classics
with open('ClassicRouteIds.csv') as f:
    classics = [line.strip() for line in f]

#initialize 'buckets'
routeid_bucket = set(classics)
userid_bucket = set()

#loop through routes and grab userids
for routeid in list(routeid_bucket)[:2]:
    try:
        userids, stars = mh.parse_stars(str(routeid))
        userset = set(userids)
        userid_bucket = userid_bucket.union(userset)
    except:
        print('Error while parsing route {}'.format(route))

#loop through userids and grab routes
for userid in list(userids)[:2]:
    try:
        routeids = mh.get_ticks(userid)
        routeset = set(routeids)
        routeid_bucket = routeid_bucket.union(routeset)
    except:
        print('Error while parsing user {}'.format(userid))

#write userids collected thus far to file:
routeID_write_loc = '/Users/colinbrochard/DSI_Capstone_local/MtProjRec/data/routeID_bucket.csv'
userID_write_loc = '/Users/colinbrochard/DSI_Capstone_local/MtProjRec/data/userID_bucket.csv'

print('writing '+ str(len(routeid_bucket))+' routes to:\n {}'.format(routeID_write_loc))
print('writing '+ str(len(userid_bucket))+' users to:\n {}'.format(userID_write_loc))

routeid_bucket_list = list(routeid_bucket)
userid_bucket_list = list(userid_bucket)
