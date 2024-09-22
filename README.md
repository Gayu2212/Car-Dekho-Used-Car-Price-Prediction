# Used Car Price Prediction

This project predicts the price of used cars based on various features such as the place, brand, year, fuel type, transmission, mileage, and ownership. The model is trained using a dataset with car data from five cities: Chennai, Bangalore, Kolkata, Hyderabad, and Delhi. The web interface is built using **Streamlit**.

## Project Structure

- `model.pkl`: Trained machine learning model using Linear Regression.
- `cleaned.csv`: Cleaned dataset of used car data.
- `app.py`: Streamlit web app for predicting used car prices based on user inputs.

## Tools and Libraries Used

- **Machine Learning**: Linear Regression is used to predict car prices.
- **Streamlit**: A Python web framework used to create the front-end interface.
- **Pandas**: For data manipulation and cleaning.
- **NumPy**: For numerical computations.
- **Pickle**: To save and load the machine learning model.

## Dataset

The dataset used for this project includes the following cities:

- Chennai
- Bangalore
- Kolkata
- Hyderabad
- Delhi

It contains information about car brands, manufacturing year, kilometers driven, fuel type, transmission, ownership type, engine capacity, power, and the number of seats.

## Model

The machine learning model was built using **Linear Regression**, which predicts car prices based on the input features. The target variable is the car price, and the features used include:

- Place (City)
- Car Brand
- Manufacturing Year
- Kilometers Driven
- Fuel Type
- Transmission Type (Manual/Automatic)
- Ownership Type (First/Second/Third Owner)
- Car Mileage
- Engine Capacity (CC)
- Maximum Power (BHP)
- Number of Seats

The input features are preprocessed and encoded to be compatible with the model.

## Web Interface

The user-friendly web interface is created using **Streamlit**. Users can select car details such as the place, brand, year, fuel type, transmission, ownership type, mileage, and more. The interface collects this information and uses the trained model to predict the price of the car.

### Features

1. **Place Selection**: The city where the car is sold.
2. **Car Brand Selection**: The brand of the car.
3. **Manufacturing Year**: A slider to input the car's manufacturing year.
4. **Fuel Type**: Select whether the car runs on petrol, diesel, CNG, or LPG.
5. **Transmission**: Choose between manual or automatic.
6. **Ownership**: The number of previous owners (First/Second/Third Owner, etc.).
7. **Car Mileage**: The mileage of the car in kilometers per liter.
8. **Engine Capacity**: Engine size in cubic centimeters (CC).
9. **Max Power**: The car's maximum power in BHP.
10. **Number of Seats**: Number of seats in the car.
11. **Kilometers Driven**: How many kilometers the car has been driven.

### Prediction

When the user enters all the details and clicks on the "Predict" button, the app uses the trained Linear Regression model to predict the price of the car and displays the result.

## How to Run the Project

1. Clone the repository:

    ```bash
    git clone 
    ```

2. Install the required libraries:

    ```bash
    pip install pandas numpy scikit-learn streamlit
    ```

3. Place the `model.pkl` and `cleaned.csv` in the project directory.

4. Run the Streamlit app:

    ```bash
    streamlit run app.py
    ```

5. The app will open in your web browser at `http://localhost:8501`.

## Code Explanation

### Model Loading

The saved Linear Regression model is loaded using `pickle`:

```python
model = pk.load(open('model.pkl', 'rb'))
