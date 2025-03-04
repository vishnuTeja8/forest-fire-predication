import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
import pickle

# Load the dataset
columns = [
    'day', 'month', 'year', 'Temperature', 'RH', 'Ws', 'Rain',
    'FFMC', 'DMC', 'DC', 'ISI', 'BUI', 'FWI', 'Classes'
]
df = pd.read_csv('data/Algerian_forest_fires_dataset.csv', skiprows=1, header=None, names=columns)

# Add the Region column
bejaia_df = df.iloc[:186].copy()
sidi_bel_abbes_df = df.iloc[186:].copy()
bejaia_df['Region'] = 0
sidi_bel_abbes_df['Region'] = 1
df = pd.concat([bejaia_df, sidi_bel_abbes_df], ignore_index=True)

# Encode the Classes column
df['Classes'] = df['Classes'].map({'not fire': 0, 'fire': 1})

# Convert columns to numeric
numeric_columns = ['day', 'month', 'year', 'Temperature', 'RH', 'Ws', 'Rain',
                   'FFMC', 'DMC', 'DC', 'ISI', 'BUI', 'FWI']
for col in numeric_columns:
    df[col] = pd.to_numeric(df[col], errors='coerce')
df.dropna(inplace=True)

# Separate features (X) and target (y)
X = df.drop(columns=['Classes'])
y = df['Classes']

# Split into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Train a Random Forest model
model = RandomForestClassifier()
model.fit(X_train, y_train)

# Save the model to a file
with open('src/model.pkl', 'wb') as f:
    pickle.dump(model, f)

print("Model saved successfully!")
# Print the column names of the training data
print(X_train.columns)