import requests, random, time, sys, json
from pymongo import MongoClient

#Input file paths:
loc_r = '/Users/colinbrochard/DSI_Capstone_local/MtProjRec/2_data/1_routeIDs/r88k/routes88k.csv'

#Establish output destinations:
client = MongoClient()
db = client.routesAPI_db
log_path = 'rAPI_log.txt'

def get_API_routes(route_IDs):
    """
    Returns list of roudids that a given userid has ticked

    Parameters:
    route_IDs: list of str

    Returns:
    routes: list of json str
    """
    time.sleep(2+.5*random.random())
    # build URL
    base_url = 'https://www.mountainproject.com/'
    query_str = 'data/get-routes?'
    route_str = ','.join(route_IDs)
    credfile = '/Users/colinbrochard/.creds/mtproj_key.txt'
    with open(credfile) as f:
        key = f.read().strip()
    url = base_url + query_str + 'routeIds=' + route_str + '&key=' + key
    # parse json and return 'ticks'
    print('GET routes: {}'.format(route_str))
    r = requests.get(url)
    parsed_json = json.loads(r.content)
    routes = parsed_json['routes']
    return routes

def write_routes_db(routes):
    """
    Writes list of users to database
    Parameters:
    routes: list of json str

    """
    for route in routes:
        print('writing to db, routes: {}'.format(route['id']))
        db.routesAPI_db.insert_one(route)
    pass

def chunks(list, n=50):
    """
    Generator function: break list into chunks of len(n)
    """
    for i in range(0, len(list), n):
        yield list[i:i+n]


def main():
    # grab routes in chunks
    with open(loc_r) as f:
        routes = [line.strip() for line in f]
    routes_chunks = chunks(routes,100) # fix this line for EC2!!!!!!!!!!
    # create logfile and direct prints to it
    old_stdout = sys.stdout
    log_file = open(log_path,"w")
    sys.stdout = log_file
    # loop through and scrape routes to db
    for chunk in routes_chunks:
        try:
            routes_data = get_API_routes(chunk)
            write_routes_db(routes_data)
        except:
            print('error while retreiving routes: {}'.format(chunk))
            time.sleep(10)
    # close logfile
    sys.stdout = old_stdout
    log_file.close()

if __name__ == '__main__':
    main()
