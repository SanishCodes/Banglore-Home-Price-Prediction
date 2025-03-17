from flask import Flask, request, jsonify
import util

app = Flask(__name__)


@app.route('/get_location_names')
def get_location_names():
    
    util.load_saved_artifacts()
    response = jsonify({
        'locations': util.get_location_names()
    })
    #print(response)
    response.headers.add("Access-Control-Allow-Origin", '*')
    return response

@app.route('/predict_home_price', methods = ['POST'])
#@app.route('/predict_home_price')
def predict_home_price():
   
    
    util.load_saved_artifacts()
    price = util.get_estimated_price('1st Phase JP Nagar',1000,2, 3)
    #return jsonify({'estimated_price': price})
    total_sqft = float(request.form['total_sqft'])
    location = request.form['location']
    bhk = int(request.form['bhk'])
    bath = int(request.form['bath'])
    
    #return total_sqft,location,bhk,bath
    response = jsonify({
        'estimated_price': util.get_estimated_price(location, total_sqft, bhk, bath)
    })

    response.headers.add('Access-Control-Allow-Origin','*')

    return response



if __name__ == '__main__':
   #predict_home_price()
   app.run()