import pandas as pd
import bson, sys, csv
from bs4 import BeautifulSoup

# path1 = '/home/ec2-user/alldumps/4_dumps/'
# path2 = ['dump_1/','dump_2/','dump_3/','dump_4/','dump_5/']
# path2a = 'routes_db/'
# path3 = ['aa','ab','ac','ad']
# paths=[]
# for x in path2:
#     for y in path3:
#         paths.append(path1 + x + path2a + y)
# files = paths[:-2]

file1 = '/home/ec2-user/alldumps/4_dumps/dump_1/routes_db/routes_db.bson'
file2 = '/home/ec2-user/alldumps/4_dumps/dump_2/routes_db/routes_db.bson'
file3 = '/home/ec2-user/alldumps/4_dumps/dump_3/routes_db/routes_db.bson'
file4 = '/home/ec2-user/alldumps/4_dumps/dump_4/routes_db/routes_db.bson'
file5 = '/home/ec2-user/alldumps/4_dumps/dump_5/routes_db/routes_db.bson'
files = [file1,file2,file3,file4,file5]

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
    for i,file in enumerate(files):
        print(file)
        print('Parsing file {} : {}'.format(i,file))
        bson_file = open(file, 'rb')
        b = bson.decode_all(bson_file.read())
        df = pd.DataFrame(b)
        data = []
        for row in df.iterrows():
            try:
                parsed = parse_stats(dict(row[1]))
                data += parsed
            except:
                print('error, row {}'.format(i))
        print('Writing file {} : {}'.format(i,file))
        with open('/Users/colinbrochard/DSI_Capstone_local/MtProjRec/2_data/rusfiles/rus_{}.csv'.format(i),'w') as out:
            csv_out=csv.writer(out)
            csv_out.writerow(['route','user','num_stars'])
            for row in data:
                csv_out.writerow(row)
        bson_file.close()

if __name__ == '__main__':
    main()
