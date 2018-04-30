import pandas as pd
import numpy as np
import json

### make these globals attributes for the init?###

inc_json = {"user_id"	:	"1234555",
	"type"	:	"Trad"	,
	"grade_low"	:	"5.8"	,
	"grade_high"	:	"5.10a"	,
	"number_pitches" : "multi-pitch",
	"location"	:	"California"	,
	"keywords"	:	["long", "commiting"]}

df_rids = pd.read_csv('/Users/colinbrochard/DSI_Capstone_local/MtProjRec/2_data/algo_rids_u5_r10')
df_r_features = pd.read_csv('/Users/colinbrochard/DSI_Capstone_local/MtProjRec/2_data/5_route_features/routes_features.csv',delimiter="|",index_col=0)
df_r_features_trim = pd.merge(df_rids, df_r_features, how='inner', left_on=['route'], right_on=['id']).drop('route',axis=1)
with open('/Users/colinbrochard/DSI_Capstone_local/MtProjRec/6_app/grade_num_map.csv') as f:
    data = [line.strip().split("|") for line in f.readlines()]
grade_num_map = {d[0]: d[1] for d in data}


#######Wrap below in class????###############

# Method filter_rows
type = inc_json['type']
grade_low_num = float(grade_num_map[inc_json['grade_low']])
grade_high_num = float(grade_num_map[inc_json['grade_high']])
number_pitches = inc_json['number_pitches']
location = inc_json['location']

df_filter = df_r_features_trim[	(df_r_features_trim['type0'] == type) &
								(df_r_features_trim['rating_num0'] >= grade_low_num) &
								(df_r_features_trim['rating_num0'] <= grade_high_num) &
								(df_r_features_trim['pitches0'] == number_pitches) &
								(df_r_features_trim['location0'] == location)]

# Method reccomend 10
df_select = df_filter.sample(10)

# Method format and JSON dumps
df_select.columns = ['route_id','route_name','type0','route_grade','rating_num0','number_pitches','location0']
df_select['estimated_stars'] = '4'
df_select['keywords'] = 'None'
df_select['route_id'] = df_select['route_id'].astype('str')
df_select.drop(['type0','rating_num0','location0'],axis=1,inplace=True)

dict_list = []
for i in range(10):
	row_dict = df_select.iloc[i].to_dict()
	row_dict['position'] = str(i)
	dict_list.append(row_dict)

out_json = json.dumps({"top_10" : dict_list })
