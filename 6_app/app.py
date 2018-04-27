from flask import Flask
app = Flask(__name__)

@app.route('/')
def return_json():
    user_id = request.args.get('user_id')
    type = request.args.get('type')
    grade_low = request.args.get('grade_low')
    grade_high = request.args.get('grade_high')
    number_pitches = request.args.get('number_pitches')
    location = request.args.get('Location')
    keywords = request.args.get('Keywords')


    return '''{'top_10' :
    	[
    		{
    		'position' 				: 1 ,
    		'route_id' 				: '123456' ,
    		'route_name' 			: 'The Nose' ,
    		'route_grade' 		: '5.9' ,
    		'number_pitches'	: 3
    		'keywords' 				: ['long','commiting'] ,
    		'estimated_stars' :	4.2
    		} ,
    		{
    		'position' 				: 2 ,
    		'route_id' 				: '123456' ,
    		'route_name' 			: 'The Nose' ,
    		'route_grade' 		: '5.9' ,
    		'number_pitches'	: 3
    		'keywords' 				: ['long','commiting'] ,
    		'estimated_stars' :	4.2
    		} ,
    		{
    		'position' 				: 3 ,
    		'route_id' 				: '123456' ,
    		'route_name' 			: 'The Nose' ,
    		'route_grade' 		: '5.9' ,
    		'number_pitches'	: 3
    		'keywords' 				: ['long','commiting'] ,
    		'estimated_stars' :	4.2
    		} ,
    		{
    		'position' 				: 4 ,
    		'route_id' 				: '123456' ,
    		'route_name' 			: 'The Nose' ,
    		'route_grade' 		: '5.9' ,
    		'number_pitches'	: 3
    		'keywords' 				: ['long','commiting'] ,
    		'estimated_stars' :	4.2
    		} ,
    		{
    		'position' 				: 5 ,
    		'route_id' 				: '123456' ,
    		'route_name' 			: 'The Nose' ,
    		'route_grade' 		: '5.9' ,
    		'number_pitches'	: 3
    		'keywords' 				: ['long','commiting'] ,
    		'estimated_stars' :	4.2
    		} ,
    		{
    		'position' 				: 6 ,
    		'route_id' 				: '123456' ,
    		'route_name' 			: 'The Nose' ,
    		'route_grade' 		: '5.9' ,
    		'number_pitches'	: 3
    		'keywords' 				: ['long','commiting'] ,
    		'estimated_stars' :	4.2
    		} ,
    		{
    		'position' 				: 7 ,
    		'route_id' 				: '123456' ,
    		'route_name' 			: 'The Nose' ,
    		'route_grade' 		: '5.9' ,
    		'number_pitches'	: 3
    		'keywords' 				: ['long','commiting'] ,
    		'estimated_stars' :	4.2
    		} ,
    		{
    		'position' 				: 8 ,
    		'route_id' 				: '123456' ,
    		'route_name' 			: 'The Nose' ,
    		'route_grade' 		: '5.9' ,
    		'number_pitches'	: 3
    		'keywords' 				: ['long','commiting'] ,
    		'estimated_stars' :	4.2
    		} ,
    		{
    		'position' 				: 9 ,
    		'route_id' 				: '123456' ,
    		'route_name' 			: 'The Nose' ,
    		'route_grade' 		: '5.9' ,
    		'number_pitches'	: 3
    		'keywords' 				: ['long','commiting'] ,
    		'estimated_stars' :	4.2
    		} ,
    		{
    		'position' 				: 10 ,
    		'route_id' 				: '123456' ,
    		'route_name' 			: 'The Nose' ,
    		'route_grade' 		: '5.9' ,
    		'number_pitches'	: 3
    		'keywords' 				: ['long','commiting'] ,
    		'estimated_stars' :	4.2
    		}
    	]
    }'''

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=80)
