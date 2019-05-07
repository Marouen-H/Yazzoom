from flask import Flask
from flask import request
from flask import jsonify
import json
from distance import getDistanceByPoint 
import pandas as pd
import pickle
import numpy as np


app = Flask(__name__)

@app.route('/')
def index():
    return "API is UP!"

@app.route('/DetectAnomalies', methods=['POST'])
def receive():
	status = 0
	e = 'None'
	res = []
	try:
		input_data = request.get_json()
	except Exception as e:
		status = 1
		return jsonify({"response" : res, "status": status, "error": e.__class__.__name__})

	try:
		model = pickle.load(open('model.pickle','rb'))
	except Exception as e:
		status = 1
		return jsonify({"response" : res, "status": status, "error": e.__class__.__name__})
	

	try:

		for d in input_data['data']: 
			print(d)
			data = pd.DataFrame(d, index=[0])
			distance = getDistanceByPoint(data, model)
			if distance.values[0] > np.float64(1.7):
				anomaly = 1
			else:
				anomaly = 0
			res.append(anomaly)
		return jsonify({"response" : res, "status": status, "error": e})
	except Exception as e:
		status = 1
		return jsonify({"response" : res, "status": status, "error": e.__class__.__name__})
	

if __name__ == '__main__':
    app.run(debug=True)