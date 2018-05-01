import pandas as pd
import numpy as np
import json, pickle
from json_handler import JsonHandler

def initialize_handler():
	df_rids = pd.read_csv('/Users/colinbrochard/DSI_Capstone_local/MtProjRec/2_data/algo_rids_u5_r10')
	df_r_features = pd.read_csv('/Users/colinbrochard/DSI_Capstone_local/MtProjRec/2_data/5_route_features/routes_features.csv',delimiter="|",index_col=0)
	df_r_features_trim = pd.merge(df_rids, df_r_features, how='inner', left_on=['route'], right_on=['id']).drop('route',axis=1)
	with open('/Users/colinbrochard/DSI_Capstone_local/MtProjRec/6_app/grade_num_map.csv') as f:
	    data = [line.strip().split("|") for line in f.readlines()]
	grade_num_map = {d[0]: d[1] for d in data}
	handler = JsonHandler(df_r_features_trim,grade_num_map)
	return handler

def main():
	handler1 = initialize_handler()
	write_loc = '/Users/colinbrochard/DSI_Capstone_local/MtProjRec/6_app/handler.pkl'
	pickle.dump(handler1, open(write_loc, 'wb'))

if __name__ == '__main__':
	main()
