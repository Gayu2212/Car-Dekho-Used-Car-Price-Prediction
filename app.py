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

