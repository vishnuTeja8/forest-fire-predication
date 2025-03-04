import pandas as pd

# Create a sample dataset
sample_data = pd.DataFrame({
    'day': [1, 2, 3, 4],
    'month': [6, 6, 7, 8],
    'year': [2012, 2012, 2012, 2012],
    'Temperature': [30, 35, 25, 32],
    'RH': [60, 40, 80, 50],
    'Ws': [15, 10, 20, 12],
    'Rain': [0, 0, 5, 0],
    'FFMC': [80, 90, 50, 85],
    'DMC': [10, 20, 5, 15],
    'DC': [20, 30, 10, 25],
    'ISI': [5, 10, 1, 7],
    'BUI': [12, 20, 5, 15],
    'FWI': [6, 15, 1, 10],
    'Region': [0, 1, 0, 1]
})

print(sample_data)

# Load the trained model
import pickle

with open('src/model.pkl', 'rb') as f:
    model = pickle.load(f)

# Make predictions
predictions = model.predict(sample_data)

# Add predictions to the sample dataset
sample_data['Predicted Classes'] = predictions

# Map predictions to human-readable labels
sample_data['Predicted Classes'] = sample_data['Predicted Classes'].map({0: 'not fire', 1: 'fire'})

# Display results
print(sample_data)