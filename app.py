from flask import Flask, request, jsonify
import geopandas as gpd
app = Flask(__name__)


@app.route('/result', methods = ['POST', 'GET'])

def result():

    data = request.get_json()
    
    for feature in data['features']:
        feature['properties']['Added Field'] = 'Totally works!'
    
    return jsonify(data), 200
