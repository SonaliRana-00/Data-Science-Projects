from flask import Flask , request, jsonify
import util

app = Flask(__name__)

@app.route('/get_location_name', methods = ['GET'])
def get_location_name():
    response = jsonify({
        'locations': util.get_location_name()
    })
    response.headers.add('Access-Control-Allow-Origin', '*')

    return response

@app.route('/predict_home_price', methods = ['Post'])
def predict_home_price():
    total_sqft = float(request.form['total_sqft'])
    loaction = request.form['location']
    bhk = int(request.form['bhk'])
    bath = int(request.form['bath'])

    response = jsonify({
        'estimated_price' : util.get_estimated_price(loaction, total_sqft, bhk,bath)
    })
    response.headers.add('Access-Control-Allow-Origin', '*')
    return response



if __name__ == '__main__':
    print('Starting Python Flask Server for Home Price Prediction')
    util.load_saved_artifacts()
    app.run()