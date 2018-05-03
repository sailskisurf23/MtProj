from json_handler_v1 import JsonHandler
import pandas as pd
import pickle

def initialize_handler():
	# grab feature data for route_ids contained in algo
	df_rids = pd.read_csv('/Users/colinbrochard/DSI_Capstone_local/MtProjRec/2_data/algo_rids_u5_r10')
	df_r_features = pd.read_csv('/Users/colinbrochard/DSI_Capstone_local/MtProjRec/2_data/5_route_features/routes_features.csv',delimiter="|",index_col=0)
	df_r_features_trim = pd.merge(df_rids, df_r_features, how='inner', left_on=['route'], right_on=['id']).drop('route',axis=1)
	# pull in model
	algo_pkl_loc = '/Users/colinbrochard/DSI_Capstone_local/MtProjRec/6_app/algo.pkl'
	algo = pickle.load(open(algo_pkl_loc, 'rb'))
	# pull in grade_num_map
	with open('/Users/colinbrochard/DSI_Capstone_local/MtProjRec/6_app/grade_num_map.csv') as f:
	    data = [line.strip().split("|") for line in f.readlines()]
	grade_num_map = {d[0]: d[1] for d in data}
	# return handler
	return JsonHandler(df_r_features_trim,algo,grade_num_map)

handler1 = initialize_handler()

inc_json = {"user_id"	:	"1234555",
	"type"	:	"Sport"	,
	"grade_low"	:	"5.10d"	,
	"grade_high"	:	"5.11b"	,
	"number_pitches" : "single-pitch",
	"location"	:	"Texas"	,
	"keywords"	:	["long", "commiting"]}

print(handler1.run_handler(inc_json))
