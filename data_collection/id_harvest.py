import MtProjScrapeHelpers as mh
from MtProjScraper import MPS





# write locations
routeID_write_loc = '/Users/colinbrochard/DSI_Capstone_local/MtProjRec/data/routeID_bucket.csv'
userID_write_loc = '/Users/colinbrochard/DSI_Capstone_local/MtProjRec/data/userID_bucket.csv'

#import routeIDs for a handful of classics
with open('ClassicRouteIds.csv') as f:
    classics = [line.strip() for line in f]
