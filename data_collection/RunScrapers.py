import requests
import urllib
import pandas as pd
from bs4 import BeautifulSoup
import os
import time
import random
import json
import pickle


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
