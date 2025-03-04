import streamlit as st
import pickle
import pandas as pd

# Load the trained model
with open('src/model.pkl', 'rb') as f:
    model = pickle.load(f)

# Title
st.title('Forest Fire Prediction')

# Input fields
temperature = st.number_input('Temperature (°C)', value=25.0)
humidity = st.number_input('Humidity (%)', value=50.0)
wind_speed = st.number_input('Wind Speed (km/h)', value=10.0)
rainfall = st.number_input('Rainfall (mm)', value=0.0)
ffmc = st.number_input('FFMC', value=50.0)
dmc = st.number_input('DMC', value=10.0)
dc = st.number_input('DC', value=20.0)
isi = st.number_input('ISI', value=5.0)
bui = st.number_input('BUI', value=15.0)
fwi = st.number_input('FWI', value=10.0)
region = st.selectbox('Region', ['Bejaia', 'Sidi-Bel Abbes'])

# Map region to numeric value
region_value = 0 if region == 'Bejaia' else 1

# Predict button
if st.button('Predict'):
    # Create a DataFrame with user inputs
    input_data = pd.DataFrame({
        'day': [1],  # Default value for day
        'month': [6],  # Default value for month
        'year': [2012],  # Default value for year
        'Temperature': [temperature],
        'RH': [humidity],
        'Ws': [wind_speed],
        'Rain': [rainfall],
        'FFMC': [ffmc],
        'DMC': [dmc],
        'DC': [dc],
        'ISI': [isi],
        'BUI': [bui],
        'FWI': [fwi],
        'Region': [region_value]
    })
     # Ensure the column order matches the training data
    input_data = input_data[['day', 'month', 'year', 'Temperature', 'RH', 'Ws', 'Rain',
                             'FFMC', 'DMC', 'DC', 'ISI', 'BUI', 'FWI', 'Region']]


    # Make prediction
    prediction = model.predict(input_data)[0]

    # Display result
    if prediction == 1:
        st.error('High Risk of Forest Fire!')
    else:
        st.success('Low Risk of Forest Fire.')