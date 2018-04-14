import requests
import urllib
import pandas as pd
from bs4 import BeautifulSoup
import os
import time
import random
import json
import pickle

def parse_stars(routeid):
'''
parameters:
routeid: string

returns:
 list of tuples with user id and number of stars given to route
'''

    #build URL
    base_url = 'https://www.mountainproject.com/'
    query_str = 'route/stats/'
    url = base_url+query_str+routeid

    #route dividers
    r = requests.get(url)
    bs_obj = BeautifulSoup(r.content, 'html.parser')
    box = bs_obj.find('table',{'class':"table table-striped"})
    containers = box.findAll('tr')

    #within container grab userID, and number of stars
    userstars = []

    for container in containers:
        href = container.a.get('href')
        userid = href.split('/')[4]
        star_count = len(container.find_all('img',{'src':"https://cdn.apstatic.com/img/stars/starBlue.svg"}))
        userstars.append((userid,star_count))

    return userstars
