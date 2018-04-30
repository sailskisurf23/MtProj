import pandas as pd
import numpy as np
import json, pickle

class JsonHandler(object):

	def __init__(self,df_r_features,grade_num_map):
		self.df_r_features = df_r_features
		self.grade_num_map = grade_num_map

	def _filter_rows(self,inc_json):
		type = inc_json['type']
		grade_low_num = float(self.grade_num_map[inc_json['grade_low']])
		grade_high_num = float(self.grade_num_map[inc_json['grade_high']])
		number_pitches = inc_json['number_pitches']
		location = inc_json['location']

		df_filter = self.df_r_features[	(self.df_r_features['type0'] == type) &
										(self.df_r_features['rating_num0'] >= grade_low_num) &
										(self.df_r_features['rating_num0'] <= grade_high_num) &
										(self.df_r_features['pitches0'] == number_pitches) &
										(self.df_r_features['location0'] == location)]
		return df_filter

	def _pick_10(self,df_filter):
		return df_filter.sample(10)

	def _return_json(self,df_select):
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
		return out_json

	def run_handler(self,inc_json):
		df_filter = self._filter_rows(inc_json)
		df_select = self._pick_10(df_filter)
		return self._return_json(df_select)
