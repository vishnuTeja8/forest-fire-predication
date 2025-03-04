import pandas as pd

# Create a realistic test dataset
test_data = pd.DataFrame({
    'day': [1, 15, 31, 10],
    'month': [6, 7, 8, 9],
    'year': [2012, 2012, 2012, 2012],
    'Temperature': [30, 42, 22, 35],  # Normal, High, Low, Moderate
    'RH': [60, 21, 90, 45],           # Normal, Low, High, Moderate
    'Ws': [15, 6, 29, 20],            # Normal, Low, High, Moderate
    'Rain': [0, 0, 16.8, 5],          # No rain, No rain, Heavy rain, Moderate rain
    'FFMC': [75, 96, 30.5, 50],       # Normal, High, Low, Moderate
    'DMC': [15, 65.9, 0.7, 20],       # Normal, High, Low, Moderate
    'DC': [50, 177.3, 7, 100],        # Normal, High, Low, Moderate
    'ISI': [5, 19, 0, 10],            # Normal, High, Low, Moderate
    'BUI': [20, 68, 1.1, 30],         # Normal, High, Low, Moderate
    'FWI': [8, 30, 0, 15],            # Normal, High, Low, Moderate
    'Region': [0, 1, 0, 1]            # Bejaia, Sidi-Bel Abbes, Bejaia, Sidi-Bel Abbes
})

print(test_data)