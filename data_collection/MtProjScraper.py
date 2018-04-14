import os
import time
import random
import csv
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

#initialize 'buckets' for routes and users:
#collected successfully, already searched, and got error trying to search
routeid_bucket = set(classics)
userid_bucket = set()

routes_searched_bucket = set()
users_searched_bucket = set()

route_errors_bucket = set()
user_errors_bucket = set()

#loop through routes and grab userids
def add_to_user_bucket(routeid_bucket,routes_searched_bucket,):
    for routeid in list(routeid_bucket.difference(routes_searched_bucket)\
    .difference(route_errors_bucket))[:2]:
        try:
            userids, stars = mh.parse_stars(str(routeid))
            userset = set(userids)
            userid_bucket = userid_bucket.union(userset)
            routes_searched_bucket = routes_searched_bucket.union(set([routeid]))

        except:
            route_errors_bucket = route_errors_bucket.union(set([routeid]))
            print('Error while parsing route {}'.format(route))
            raise

def add_to_route_bucket(userid_bucket):
    for userid in list(userid_bucket.difference(users_searched_bucket)\
    .difference(user_errors_bucket))[:2]:
        try:
            routeids = mh.get_ticks(userid)
            routeset = set(routeids)
            routeid_bucket = routeid_bucket.union(routeset)
            users_searched_bucket = users_searched_bucket.union(set([userid]))

        except:
            user_errors_bucket = user_errors_bucket.union(set([userid]))
            print('Error while parsing user {}'.format(userid))
            raise
    return routeid_bucket

#write userids and routeids collected thus far to file:
routeID_write_loc = '/Users/colinbrochard/DSI_Capstone_local/MtProjRec/data/routeID_bucket.csv'
userID_write_loc = '/Users/colinbrochard/DSI_Capstone_local/MtProjRec/data/userID_bucket.csv'

#write routes
print('writing '+ str(len(routeid_bucket))+' routes to:\n {}'\
.format(routeID_write_loc))
routeid_bucket_list = list(routeid_bucket)
with open(routeID_write_loc,'w') as f1:
    wr = csv.writer(f1)
    for id in routeid_bucket_list:
        wr.writerow([id])

#write users
print('writing '+ str(len(userid_bucket))+' users to:\n {}'\
.format(userID_write_loc))
userid_bucket_list = list(userid_bucket)
with open(userID_write_loc,'w') as f2:
    wr = csv.writer(f2)
    for id in userid_bucket_list:
        wr.writerow([id])




#output errorlog

#user_errors_bucket_list = list(user_errors_bucket)
#route_errors_bucket_list = list(route_errors_bucket)
