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



#initialize 'buckets' for routes and users:
#collected successfully, already searched, and got error trying to search
class MPS(object):

    def __init__(self,startroutes):
        self.routeid_bucket = set(startroutes)
        self.userid_bucket = set()

        self.routes_searched_bucket = set()
        self.users_searched_bucket = set()

        self.route_errors_bucket = set()
        self.user_errors_bucket = set()

    #loop through routes and grab userids
    def add_to_user_bucket(self):
        for routeid in list(self.routeid_bucket\
        .difference(self.routes_searched_bucket)\
        .difference(self.route_errors_bucket)):
            try:
                userids, stars = mh.parse_stars(str(routeid))
                userset = set(userids)
                self.userid_bucket = self.userid_bucket.union(userset)
                self.routes_searched_bucket = self.routes_searched_bucket\
                                                    .union(set([routeid]))

            except:
                self.route_errors_bucket = self.route_errors_bucket\
                                                .union(set([routeid]))
                print('Error while parsing route {}'.format(route))
                raise

    def add_to_route_bucket(self):
        for userid in list(self.userid_bucket\
        .difference(self.users_searched_bucket)\
        .difference(self.user_errors_bucket)):
            try:
                routeids = mh.get_ticks(userid)
                routeset = set(routeids)
                self.routeid_bucket = self.routeid_bucket.union(routeset)
                self.users_searched_bucket = self.users_searched_bucket\
                                                    .union(set([userid]))

            except:
                self.user_errors_bucket = self.user_errors_bucket\
                                                .union(set([userid]))
                print('Error while parsing user {}'.format(userid))
                raise
        return routeid_bucket

    def write_routes(self,loc):
        print('writing '+ str(len(self.routeid_bucket))
                +' routes to:\n {}'.format(loc))
        routeid_list = list(self.routeid_bucket)
        with open(loc,'w+') as f:
            wr = csv.writer(f)
            for id in routeid_list:
                wr.writerow([id])

    def write_users(self,loc):
        print('writing '+ str(len(self.userid_bucket))
                +' users to:\n {}'.format(loc))
        userid_list = list(self.userid_bucket)
        with open(loc,'w+') as f:
            wr = csv.writer(f)
            for id in userid_list:
                wr.writerow([id])

    def write_routes(self,loc):
        print('writing '+ str(len(self.routeid_bucket))
                +' routes to:\n {}'.format(loc))
        routeid_list = list(self.routeid_bucket)
        with open(loc,'w+') as f:
            wr = csv.writer(f)
            for id in routeid_list:
                wr.writerow([id])






# write locations
routeID_write_loc = '/Users/colinbrochard/DSI_Capstone_local/MtProjRec/data/routeID_bucket.csv'
userID_write_loc = '/Users/colinbrochard/DSI_Capstone_local/MtProjRec/data/userID_bucket.csv'

#import routeIDs for a handful of classics
with open('ClassicRouteIds.csv') as f:
    classics = [line.strip() for line in f]






#output errorlog

#user_errors_bucket_list = list(user_errors_bucket)
#route_errors_bucket_list = list(route_errors_bucket)
