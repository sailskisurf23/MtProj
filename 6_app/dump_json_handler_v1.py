import pandas as pd
import numpy as np
import json, pickle
from json_handler_v1 import JsonHandler

# paths in
algo_pkl_loc = '/Users/colinbrochard/DSI_Capstone_local/MtProjRec/6_app/algo.pkl'
algo_rids_loc = '/Users/colinbrochard/DSI_Capstone_local/MtProjRec/2_data/algo_rids.csv'
features_loc = '/Users/colinbrochard/DSI_Capstone_local/MtProjRec/2_data/5_route_features/routes_features.csv'
grade_num_map_loc = '/Users/colinbrochard/DSI_Capstone_local/MtProjRec/6_app/grade_num_map.csv'
# path out
write_loc = '/Users/colinbrochard/DSI_Capstone_local/MtProjRec/6_app/handler_v1.pkl'

def initialize_handler():
	# grab feature data for route_ids contained in algo
	df_rids = pd.read_csv(algo_rids_loc)
	df_r_features = pd.read_csv(features_loc,delimiter="|",index_col=0)
	df_r_features_trim = pd.merge(df_rids, df_r_features,
									how='inner', left_on=['route'], right_on=['id'])\
									.drop('route',axis=1)
	# pull in model
	algo = pickle.load(open(algo_pkl_loc, 'rb'))
	# pull in grade_num_map
	with open(grade_num_map_loc) as f:
	    data = [line.strip().split("|") for line in f.readlines()]
	grade_num_map = {d[0]: d[1] for d in data}
	# return handler
	return JsonHandler(df_r_features_trim, algo, grade_num_map)

def main():
	handler1 = initialize_handler()
	pickle.dump(handler1, open(write_loc, 'wb'))

if __name__ == '__main__':
	main()
