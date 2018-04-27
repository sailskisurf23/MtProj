import pandas as pd
import bson, sys, csv, pymongo
from bs4 import BeautifulSoup
from pymongo import MongoClient

write_loc = '/home/ec2-user/rusfiles'

client = MongoClient()
db = client.routes_db
collections = [db.dump1, db.dump2, db.dump3, db.dump4, db.dump5]

def parse_stats(entry):
    """
    Takes a mongo entry and returns list of tuples (routeid, userid, num_stars)

    --Parameters--
    entry: dict

    --Returns--
    list of tuples
    """
    stats = entry['stats']
    routeid = entry['routeid']
    try:
        bs_obj = BeautifulSoup(stats, 'html.parser')
        box = bs_obj.find('table', {'class': "table table-striped"})
        containers = box.findAll('tr')

        # within container grab userID, and number of stars
        routeids = []
        userids = []
        star_counts = []
        for container in containers:
            href = container.a.get('href')
            userid = href.split('/')[4]
            star_count = len(container.find_all('img', {'src': "https://cdn.apstatic.com/img/stars/starBlue.svg"}))
            routeids.append(routeid)
            userids.append(userid)
            star_counts.append(star_count)
        return [tup for tup in zip(routeids,userids,star_counts)]
    except:
        print('error parsing route: {}'.format(routeid))

def main():
    for i,collection in enumerate(collections):
        print('Reading in dump_{}'.format(i+1))
        df = pd.DataFrame(list(collection.find()))
        print('Parsing dump_{}'.format(i+1))
        data = []
        for row in df.iterrows():
            try:
                parsed = parse_stats(dict(row[1]))
                data += parsed
            except:
                print('error while parsing')
        print('Writing dump_{}'.format(i+1))
        print('To ' + write_loc + 'rus_{}.csv'.format(i+1))
        with open(write_loc + 'rus_{}.csv'.format(i+1),'w') as out:
            csv_out=csv.writer(out)
            csv_out.writerow(['route','user','num_stars'])
            for row in data:
                csv_out.writerow(row)

if __name__ == '__main__':
    main()
