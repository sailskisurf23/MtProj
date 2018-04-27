import pandas as pd
import bson, sys, csv, pymongo
from bs4 import BeautifulSoup
from pymongo import MongoClient


# path1 = '/home/ec2-user/alldumps/4_dumps/'
# path2 = ['dump_1/','dump_2/','dump_3/','dump_4/','dump_5/']
# path2a = 'routes_db/'
# path3 = ['r1.bson','r2.bson','r3.bson','r4.bson']
# paths=[]
# for x in path2:
#     for y in path3:
#         paths.append(path1 + x + path2a + y)
# files = paths[:-2]
# write_loc = '/home/ec2-user/rusfiles/'

#
# path1 = '/Users/colinbrochard/DSI_Capstone_local/MtProjRec/2_data/4_dumps/'
# path2 = ['dump_1/','dump_2/']
# path2a = 'routes_db/'
# path3 = ['aa','ab','ac','ad']
# paths=[]
# for x in path2:
#     for y in path3:
#         paths.append(path1 + x + path2a + y)
# files = paths

write_loc = '/Users/colinbrochard/DSI_Capstone_local/MtProjRec/2_data/3_rus/rusfiles'

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
    # for i,file in enumerate(files):
    #     print(file)
    #     print('Parsing file {} : {}'.format(i,file))
    #     bson_file = open(file, 'rb')
    #     b = bson.decode_all(bson_file.read())
    #     df = pd.DataFrame(b)
    #     data = []
    #     bson_file.close() ###
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
