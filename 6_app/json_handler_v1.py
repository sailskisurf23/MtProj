# This module is used to process incoming JSON query strings from app
# Returns list of top 10 recommended routes using alogrithm in INIT
import pandas as pd
import numpy as np
import json, pickle
from surprise import AlgoBase, Dataset, evaluate, accuracy, SVD, Reader
from surprise.model_selection import train_test_split

class JsonHandler(object):

	def __init__(self,df_r_features,algo,grade_num_map):
		self.df_r_features = df_r_features
		self.algo = algo
		self.grade_num_map = grade_num_map

	def _filter_rows(self,inc_json):
		# parse incoming json
		type = inc_json['type']
		grade_low_num = float(self.grade_num_map[inc_json['grade_low']])
		grade_high_num = float(self.grade_num_map[inc_json['grade_high']])
		number_pitches = inc_json['number_pitches']
		location = inc_json['location']
		# filter features df based on info contained in json
		df_filter = self.df_r_features[	(self.df_r_features['type0'] == type) &
										(self.df_r_features['rating_num0'] >= grade_low_num) &
										(self.df_r_features['rating_num0'] <= grade_high_num) &
										(self.df_r_features['pitches0'] == number_pitches) &
										(self.df_r_features['location0'] == location)]
		return df_filter

	def _pick_10(self,df_filter,inc_json):
		user_id = inc_json['user_id']
		route_ids = df_filter['id'].values
		# construct matrix to predict
		mat_in = np.zeros((len(route_ids),3))
		mat_in[:,0] = user_id
		mat_in[:,1] = route_ids
		# read into suprise "testset" form
		reader = Reader(line_format='user item rating', sep=',', skip_lines=1)
		data_in = Dataset.load_from_df(pd.DataFrame(mat_in.astype(int)),reader=reader)
		test_in = data_in.construct_testset(data_in.raw_ratings)
		# use algo make predictions and sort
		preds = self.algo.test(test_in)
		df_preds10 = pd.DataFrame(preds).sort_values('est',ascending=False).iloc[:10,:]
		# return features df with 10 predictions
		return pd.merge(df_preds10, df_filter, how='inner', left_on=['iid'], right_on=['id']).drop(['uid','iid','r_ui','details'],axis=1)

	def _return_json(self,df_select):
		df_select.columns = ['estimated_stars','route_id','route_name','type0','route_grade','rating_num0','number_pitches','location0']
		df_select['keywords'] = 'None'
		df_select['route_id'] = df_select['route_id'].astype('str')
		df_select.drop(['type0','rating_num0','location0'],axis=1,inplace=True)

		dict_list = []
		for i in range(10):
			row_dict = df_select.iloc[i].to_dict()
			row_dict['position'] = str(i)
			dict_list.append(row_dict)
		out_json = json.dumps({"top_10" : dict_list })
		return out_json

	def run_handler(self,inc_json):
		df_filter = self._filter_rows(inc_json)
		df_select = self._pick_10(df_filter,inc_json)
		return self._return_json(df_select)
