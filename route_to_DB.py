import requests, random, time, sys
from pymongo import MongoClient

#Input file paths:
loc_r = '/Users/colinbrochard/DSI_Capstone_local/MtProjRec/data1/routes4.csv'
base_url = 'https://www.mountainproject.com/'

#Establish output destinations:
client = MongoClient() # adjust this line when wrting to s3 bucket to include s3 url/port info?
db = client.routes_db
log_path = 'log_tester.txt'

def route_to_db(base_url,routeid):
        '''
        Scrape contents of route description and route stats page; write to MongoDBself.

        Parameters
        base_url (str)
        routeid (str)

        '''
        #build URLs
        url1 = base_url+'route/'+routeid
        url2 = base_url+'route/stats/'+routeid
        #retrieve URLs
        time.sleep(2+random.random())
        r1 = requests.get(url1)
        time.sleep(2+random.random())
        r2 = requests.get(url2)
        #create dict with retreived data, write to MongoDB
        d = {'routeid' : routeid,
            'page' : r1.content,
            'stats' : r2.content}
        print('writing to db, route: {}'.format(routeid))
        db.routes_db.insert_one(d)
        pass

def main():
    #establish base url and grab list of routes
    with open(loc_r) as f:
        routes = [line.strip() for line in f]
    #create logfile and direct prints to it
    old_stdout = sys.stdout
    log_file = open(log_path,"w")
    sys.stdout = log_file
    #loop through and scrape routes to db
    for i,routeid in enumerate(routes[60:62]):
        try:
            print('retrieving route: {}'.format(routeid))
            print('{} / {} routes completed'.format(i,len(routes)))
            route_to_db(base_url, routeid)
        except:
            print('error while retreving route: {}'.format(routeid))
            time.sleep(10)

    sys.stdout = old_stdout
    log_file.close()

if __name__ == '__main__':
    main()













#log fle
#  seed with where kleft offers
