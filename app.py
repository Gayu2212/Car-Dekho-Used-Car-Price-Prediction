import pandas as pd 
import numpy as np 
import pickle as pk 
import streamlit as st

# Load the trained model
model = pk.load(open('model.pkl','rb'))

# Set the title and apply some styling using HTML and CSS
st.markdown("""
    <style>
    body {
            background-color: #00FFFF; /* Aqua blue background */
        }
        .header {
            font-size: 50px;
            color: #4CAF50;
            text-align: center;
            font-family: 'Helvetica', sans-serif;
        }
        .subheader {
            font-size: 30px;
            color: #333;
            text-align: center;
            font-family: 'Helvetica', sans-serif;
        }
        .predict-button {
            background-color: #4CAF50;
            color: white;
            border-radius: 10px;
            width: 150px;
            height: 50px;
            font-size: 18px;
        }
        .output {
            font-size: 20px;
            color: #FF5733;
            text-align: center;
            font-weight: bold;
        }
    </style>
    <div class="header">Car Dekho Used Car Price Prediction</div>
""", unsafe_allow_html=True)

# Load the cleaned car data
cars_data = pd.read_csv('cleaned.csv')

# Create a form layout for better UX
st.markdown('<div class="subheader">Enter Car Details Below</div>', unsafe_allow_html=True)
st.markdown("---")

# Create a two-column layout for better arrangement of inputs
col1, col2 = st.columns(2)

with col1:
    place = st.selectbox('Select the Place', cars_data['place'].unique())
    name = st.selectbox('Select Car Brand', cars_data['model'].unique())
    year = st.slider('Car Manufactured Year', 1994, 2024)
    km_driven = st.slider('No of kms Driven', 11, 200000)

with col2:
    fuel = st.selectbox('Fuel Type', cars_data['fuel_type'].unique())
    transmission = st.selectbox('Transmission Type', cars_data['transmission'].unique())
    owner = st.selectbox('Ownership Type', cars_data['ownership'].unique())
    mileage = st.slider('Car Mileage (km/l)', 10, 40)
    engine = st.slider('Engine CC', 700, 5000)
    max_power = st.slider('Max Power (BHP)', 0, 200)
    seats = st.slider('No of Seats', 5, 10)

# Add the prediction button with custom styling
if st.button("Predict", key='predict', help="Click to predict the car price"):
    # Prepare the input data for the model
    input_data_model = pd.DataFrame(
        [[transmission, name, year, fuel, seats, km_driven, owner, engine, max_power, mileage, place]],
        columns=['transmission', 'model', 'modelyear', 'fuel_type', 'seats', 'kms_driven', 'ownership', 'engine', 'max_power', 'mileage', 'place']
    )

    # Data preprocessing (as per original code)
    input_data_model['ownership'].replace(['First Owner', 'Second Owner', 'Third Owner', 'Fourth & Above Owner', 'Test Drive Car'], [1, 2, 3, 4, 5], inplace=True)
    input_data_model['fuel_type'].replace(['Diesel', 'Petrol', 'LPG', 'CNG'], [1, 2, 3, 4], inplace=True)
    input_data_model['transmission'].replace(['Manual', 'Automatic'], [1, 2], inplace=True)
    input_data_model['model'].replace(
        ['Maruti', 'Skoda', 'Honda', 'Hyundai', 'Toyota', 'Ford', 'Renault', 'Mahindra', 'Tata', 'Chevrolet', 'Datsun', 'Jeep', 
        'Mercedes-Benz', 'Mitsubishi', 'Audi', 'Volkswagen', 'BMW', 'Nissan', 'Lexus', 'Jaguar', 'Land', 'MG', 'Volvo', 'Daewoo', 
        'Kia', 'Fiat', 'Force', 'Ambassador', 'Ashok', 'Isuzu', 'Opel'], 
        range(1, 32), inplace=True
    )
    input_data_model['place'].replace(['Chennai', 'Bangalore', 'Delhi', 'Hyderabad', 'Kolkata'], [1, 2, 3, 4, 5], inplace=True)
    
    # Predict the price using the loaded model
    car_price = model.predict(input_data_model)

    # Display the output price with styling
    st.markdown(f'<div class="output">Predicted Car Price: ₹ {car_price[0]:,.2f}</div>', unsafe_allow_html=True)

# from flask import Flask, render_template, request, jsonify
# import pandas as pd
# import pickle as pk

# app = Flask(__name__)

# # Load the model
# model = pk.load(open('model.pkl', 'rb'))

# # Route to render HTML
# @app.route('/')
# def index():
#     return render_template('index.html')

# # Route to handle form submission and return prediction
# @app.route('/predict', methods=['POST'])
# def predict():
#     # Extract form data
#     place = int(request.form['place'])
#     name = int(request.form['model'])
#     year = int(request.form['year'])
#     kms_driven = int(request.form['kms_driven'])
#     fuel = int(request.form['fuel'])
#     transmission = int(request.form['transmission'])
#     owner = int(request.form['owner'])
#     mileage = float(request.form['mileage'])
#     engine = int(request.form['engine'])
#     max_power = float(request.form['max_power'])
#     seats = int(request.form['seats'])

#     # Create input data for the model
#     input_data_model = pd.DataFrame([[transmission, name, year, fuel, seats, kms_driven, owner, engine, max_power, mileage, place]], 
#                                     columns=['transmission', 'model', 'modelyear', 'fuel_type', 'seats', 'kms_driven', 'ownership', 'engine', 'max_power', 'mileage', 'place'])
    
#     # Model expects specific numerical replacements
#     car_price = model.predict(input_data_model)

#     # Return prediction as JSON
#     return jsonify({'price': car_price[0]})

# if __name__ == '__main__':
#     app.run(debug=True)
