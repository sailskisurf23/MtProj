import requests
from bs4 import BeautifulSoup
import random
import json

# import pandas as pd
# import numpy as np
# import time


def get_ticks(userId):
    """
    Returns list of roudids that a given userid has ticked

    Parameters:
    userid: string

    Returns:
    list
    """
    #build URL
    base_url = 'https://www.mountainproject.com/'
    query_str = 'data/get-ticks?'
    user = userId
    credfile = '/Users/colinbrochard/.creds/mtproj_key.txt'
    with open(credfile) as f:
        key=f.read().strip()
    url = base_url+query_str+'userId='+user+'&key='+key
    #parse json and return 'ticks'
    r = requests.get(url)
    parsed_json = json.loads(r.content)
    return parsed_json

def get_userids_for_zip(zip):
    """
    Returns list of userids for a given zipcode

    Parameters:
    zip: string

    Returns:
    list
    """
    search_url = 'https://www.mountainproject.com/partner-finder/results?distance=50&location='+zip
    r = requests.get(search_url)
    bs_obj = BeautifulSoup(r.content, 'html.parser')
    containers = bs_obj.findAll('div',{'class':'name-location'})
    ID_list = []
    for container in containers:
        href = container.a.get('href')
        id = href[href.find('user/')+5:href.find('user/')+14]
        ID_list.append(id.split('/')[0])
    return ID_list

def parse_stars(routeid):
    """
    Get all user ratings for a given routeid.

    Parameters:
    routeid -- string

    Returns:
    userids -- ID_list
    star_counts -- ID_list
    """
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
    userids = []
    star_counts = []

    for container in containers:
        href = container.a.get('href')
        userid = href.split('/')[4]
        star_count = len(container.find_all('img',{'src':"https://cdn.apstatic.com/img/stars/starBlue.svg"}))
        userids.append(userid)
        star_counts.append(star_count)


    return userids,star_counts
