import pandas as pd
import numpy as np


inc_json = {"user_id"	:	"1234555",
	"type"	:	"Trad"	,
	"grade_low"	:	"5.8"	,
	"grade_high"	:	"5.10"	,
	"number_pitches" : "multi-pitch",
	"Location"	:	"California"	,
	"Keywords"	:	["long", "commiting"]}

df_rids = pd.read_csv('/Users/colinbrochard/DSI_Capstone_local/MtProjRec/2_data/algo_rids_u5_r10')
df_r_features = pd.read_csv('/Users/colinbrochard/DSI_Capstone_local/MtProjRec/2_data/5_route_features/routes_features.csv',delimiter="|",index_col=0)
df_r_features_trim = pd.merge(df_rids, df_r_features, how='inner', left_on=['route'], right_on=['id']).drop('route',axis=1)
