from flask import Flask, request, jsonify
import pickle
import numpy as np

app = Flask(__name__)

# 1. Load the AI Brain into RAM
model_path = 'Crop_Recommendation.pkl'
model = pickle.load(open(model_path, 'rb'))

@app.route('/predict', methods=['POST'])
def predict():
    try:
        # 2. Get the data from Next.js
        data = request.get_json()
        
        # 3. Extract the 7 values
        features = np.array([[
            data['N'], 
            data['P'], 
            data['K'], 
            data['temperature'], 
            data['humidity'], 
            data['ph'], 
            data['rainfall']
        ]])
        
        # 4. Make Prediction
        prediction = model.predict(features)
        
        # 5. Send back to Next.js
        return jsonify({'recommended_crop': prediction[0]})
        
    except Exception as e:
        return jsonify({'error': str(e)})

if __name__ == '__main__':
    # Run on port 5000
    app.run(host='0.0.0.0', port=5000, debug=True)