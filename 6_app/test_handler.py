from json_handler import JsonHandler
import pickle

inc_json = {"user_id"	:	"1234555",
	"type"	:	"Sport"	,
	"grade_low"	:	"5.10d"	,
	"grade_high"	:	"5.11b"	,
	"number_pitches" : "single-pitch",
	"location"	:	"Texas"	,
	"keywords"	:	["long", "commiting"]}

handler_pkl_loc = '/home/ec2-user/handler.pkl'
handler1 = pickle.load(open(handler_pkl_loc, 'rb'))

print(handler1.run_handler(inc_json))
