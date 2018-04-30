from flask import Flask, request, jsonify
from flask_cors import CORS
import json

app = Flask(__name__)
CORS(app)

@app.route('/', methods = ['POST'])
def return_json():
    content = request.get_json()

    try:
        id = content['user_id']
        print('Return 10 Recommendations for {}'.format(id))
    except:
        print('cant find user_id')


    response = jsonify({"top_10" :
    	[
    		{
    		"position" 				: 1 ,
    		"route_id" 				: "123456" ,
    		"route_name" 			: "The Nose" ,
    		"route_grade" 		: "5.9" ,
    		"number_pitches"	: 3,
    		"keywords" 				: ["long","commiting"] ,
    		"estimated_stars" :	4.2
    		} ,
    		{
    		"position" 				: 2 ,
    		"route_id" 				: "123456" ,
    		"route_name" 			: "The Nose" ,
    		"route_grade" 		: "5.9" ,
    		"number_pitches"	: 3,
    		"keywords" 				: ["long","commiting"] ,
    		"estimated_stars" :	4.2
    		} ,
    		{
    		"position" 				: 3 ,
    		"route_id" 				: "123456" ,
    		"route_name" 			: "The Nose" ,
    		"route_grade" 		: "5.9" ,
    		"number_pitches"	: 3,
    		"keywords" 				: ["long","commiting"] ,
    		"estimated_stars" :	4.2
    		} ,
    		{
    		"position" 				: 4 ,
    		"route_id" 				: "123456" ,
    		"route_name" 			: "The Nose" ,
    		"route_grade" 		: "5.9" ,
    		"number_pitches"	: 3,
    		"keywords" 				: ["long","commiting"] ,
    		"estimated_stars" :	4.2
    		} ,
    		{
    		"position" 				: 5 ,
    		"route_id" 				: "123456" ,
    		"route_name" 			: "The Nose" ,
    		"route_grade" 		: "5.9" ,
    		"number_pitches"	: 3,
    		"keywords" 				: ["long","commiting"] ,
    		"estimated_stars" :	4.2
    		} ,
    		{
    		"position" 				: 6 ,
    		"route_id" 				: "123456" ,
    		"route_name" 			: "The Nose" ,
    		"route_grade" 		: "5.9" ,
    		"number_pitches"	: 3,
    		"keywords" 				: ["long","commiting"] ,
    		"estimated_stars" :	4.2
    		} ,
    		{
    		"position" 				: 7 ,
    		"route_id" 				: "123456" ,
    		"route_name" 			: "The Nose" ,
    		"route_grade" 		: "5.9" ,
    		"number_pitches"	: 3,
    		"keywords" 				: ["long","commiting"] ,
    		"estimated_stars" :	4.2
    		} ,
    		{
    		"position" 				: 8 ,
    		"route_id" 				: "123456" ,
    		"route_name" 			: "The Nose" ,
    		"route_grade" 		: "5.9" ,
    		"number_pitches"	: 3,
    		"keywords" 				: ["long","commiting"] ,
    		"estimated_stars" :	4.2
    		} ,
    		{
    		"position" 				: 9 ,
    		"route_id" 				: "123456" ,
    		"route_name" 			: "The Nose" ,
    		"route_grade" 		: "5.9" ,
    		"number_pitches"	: 3,
    		"keywords" 				: ["long","commiting"] ,
    		"estimated_stars" :	4.2
    		} ,
    		{
    		"position" 				: 10 ,
    		"route_id" 				: "123456" ,
    		"route_name" 			: "The Nose" ,
    		"route_grade" 		: "5.9" ,
    		"number_pitches"	: 3,
    		"keywords" 				: ["long","commiting"] ,
    		"estimated_stars" :	4.2
    		}
    	]
    })
    return response

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=80)
