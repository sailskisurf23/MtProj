import requests
import urllib
import pandas as pd
from bs4 import BeautifulSoup
import os
import time
import random
import json
import pickle

class AppURLopener(urllib.request.FancyURLopener):
    version = "Mozilla/5.0"

def get_user_ticks(userId):

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

def get_userids(zip):
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

def main():
    with open ('CO_users.txt', 'rb') as fp:
        ids = pickle.load(fp)
    dump_dir = '/Users/colinbrochard/DSI_Capstone/MtProj/data_collection/user_ticks_CO1/'
    os.mkdir(dump_dir)
    for id in ids:
        trailer = '.txt'
        with open(dump_dir+id+trailer, 'w') as outfile:
            time.sleep(random.random()*2)
            data = get_user_ticks(id)
            json.dump(data, outfile)


if __name__ == '__main__':
    main()
