from flask import Flask, request, jsonify
from flask_cors import CORS
from json_handler import JsonHandler
import json, pickle
app = Flask(__name__)
CORS(app)

handler_pkl_loc = '/Users/colinbrochard/DSI_Capstone_local/MtProjRec/6_app/handler.pkl'
handler1 = pickle.load(open(handler_pkl_loc, 'rb'))

@app.route('/', methods = ['POST'])
def return_json():
    inc_json = request.get_json()
    try:
        id = content['user_id']
        print('Return 10 Recommendations for {}'.format(id))
        return handler1.run_handler(inc_json)
    except:
        print('cant find user_id')

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=80)
