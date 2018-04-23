import csv
import mt_scrape_helpers as mh


class MPS(object):
    """Scraper object build for harvesting routeIDs and userIDs from MtProj

    Attributes:
        routeID_bucket (set): routeIDs harvested
        routes_searched_bucket (set): routes already searched
        route_errors_bucket (set): error when accessing these routes
        userID_bucket (set): users harvested
        users_searched_bucket (set): routes already searched
        user_errors_bucket (set): error when searching these users
    """

    def __init__(self, startusers=None, startroutes=None):
        """Initalize scraper object with a handful of popular routes

        Args:
            startroutes (list): initalize scraper object with a handful of popular routes
        """
        self.routeID_bucket = set(startroutes)
        self.userID_bucket = set(startusers)

        self.routes_searched_bucket = set()
        self.users_searched_bucket = set()

        self.route_errors_bucket = set()
        self.user_errors_bucket = set()


    def run_scraper(self, n):
        """
        Loop through add to bucket calls n times
        """
        for _ in range(n):
            self.add_to_user_bucket()
            self.add_to_route_bucket()

    def add_to_user_bucket(self, n=None):
        """
        Loop through routeID_bucket, parse userIDs from route page,
        and add to userID_bucket. Omits routeIDs already searched.
        """

        if n==None:
            print('Looking through {} routes'.format(len(self.routeID_bucket)))
        else:
            print('Looking through {} routes'.format(n))

        for routeID in list(self.routeID_bucket
                                .difference(self.routes_searched_bucket)
                                .difference(self.route_errors_bucket))[:n]:
            try:
                userIDs, stars = mh.parse_stars(str(routeID))
                userset = set(userIDs)
                self.userID_bucket = self.userID_bucket.union(userset)
                self.routes_searched_bucket = self.routes_searched_bucket.union(set([routeID]))

            except:
                self.route_errors_bucket = self.route_errors_bucket.union(set([routeID]))
                print('Error while parsing route {}'.format(routeID))
                raise

    def add_to_route_bucket(self,n=None):
        """
        Loop through userID_bucket, parse routeIDs from users ticklist,
        and add to routeID_bucket. Omits userIDs already searched.
        """
        if n==None:
            print('Looking through {} users'.format(len(self.userID_bucket)))
        else:
            print('Looking through {} users'.format(n))

        for userID in list(self.userID_bucket
                               .difference(self.users_searched_bucket)
                               .difference(self.user_errors_bucket))[:n]:
            try:
                routeIDs = mh.get_ticks(userID)
                routeset = set(routeIDs)
                self.routeID_bucket = self.routeID_bucket.union(routeset)
                self.users_searched_bucket = self.users_searched_bucket.union(set([userID]))

            except:
                self.user_errors_bucket = self.user_errors_bucket\
                                                .union(set([userID]))
                print('Error while parsing user {}'.format(userID))
                raise

    def write_routes(self, loc):
        """
        Write all routes in routeID_bucket to csv

        Args:
            loc (str): location to write csv
        """
        print('writing ' + str(len(self.routeID_bucket)) + ' routes to:\n {}'.format(loc))
        routeID_list = list(self.routeID_bucket)
        with open(loc, 'w+') as f:
            wr = csv.writer(f)
            for routeID in routeID_list:
                wr.writerow([routeID])

    def write_users(self, loc):
        """
        Write all users in userID_bucket to csv

        Args:
            loc (str): location to write csv
        """
        print('writing ' + str(len(self.userID_bucket)) + ' users to:\n {}'.format(loc))
        userID_list = list(self.userID_bucket)
        with open(loc, 'w+') as f:
            wr = csv.writer(f)
            for userID in userID_list:
                wr.writerow([userID])

    def write_route_errors(self, loc):
        """
        Write all routeIDs in route_errors_bucket to csv

        Args:
            loc (str): location to write csv
        """
        print('writing ' + str(len(self.route_errors_bucket)) + ' routes to:\n {}'.format(loc))
        route_errors_list = list(self.route_errors_bucket)
        with open(loc, 'w+') as f:
            wr = csv.writer(f)
            for error in route_errors_list:
                wr.writerow([error])

    def write_user_errors(self, loc):
        """
        Write all userIDs in user_errors_bucket to csv

        Args:
            loc (str): location to write csv
        """
        print('writing ' + str(len(self.user_errors_bucket)) + ' routes to:\n {}'.format(loc))
        user_errors_list = list(self.user_errors_bucket)
        with open(loc,'w+') as f:
            wr = csv.writer(f)
            for error in user_errors_list:
                wr.writerow([error])
