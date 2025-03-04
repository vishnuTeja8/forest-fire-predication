import pandas as pd

# Load the dataset
df = pd.read_csv('data/Algerian_forest_fires_dataset.csv', skiprows=1, header=None)

# Assign column names based on the dataset description
columns = [
    'day', 'month', 'year', 'Temperature', 'RH', 'Ws', 'Rain', 
    'FFMC', 'DMC', 'DC', 'ISI', 'BUI', 'FWI', 'Classes'
]
df.columns = columns

# Split the dataset into two regions
bejaia_df = df.iloc[:186].copy()  # First 186 rows for Bejaia
sidi_bel_abbes_df = df.iloc[186:].copy()  # Remaining rows for Sidi-Bel Abbes

# Add a 'Region' column
bejaia_df['Region'] = 0  # Bejaia = 0
sidi_bel_abbes_df['Region'] = 1  # Sidi-Bel Abbes = 1

# Combine the two datasets
df = pd.concat([bejaia_df, sidi_bel_abbes_df], ignore_index=True)

# Convert columns to numeric
numeric_columns = ['day', 'month', 'year', 'Temperature', 'RH', 'Ws', 'Rain',
                   'FFMC', 'DMC', 'DC', 'ISI', 'BUI', 'FWI']

for col in numeric_columns:
    df[col] = pd.to_numeric(df[col], errors='coerce')

# Encode 'Classes' column: 'not fire' -> 0, 'fire' -> 1
df['Classes'] = df['Classes'].map({'not fire': 0, 'fire': 1})

# Drop rows with NaN values caused by conversion
df.dropna(inplace=True)

# Reset index after dropping rows
df.reset_index(drop=True, inplace=True)

# Check the result
print(df[['Region', 'Classes']].head())
print(df[['Region', 'Classes']].tail())

# Features (X) and target (y)
X = df.drop(columns=['Classes'])  # Drop the target column
y = df['Classes']  # Target column

print("Shape of X:", X.shape)
print("Shape of y:", y.shape)

from sklearn.model_selection import train_test_split

# Split into 80% training and 20% testing
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score
# Initialize and train Random Forest
rf_model = RandomForestClassifier()
rf_model.fit(X_train, y_train)

# Predict and evaluate
y_pred_rf = rf_model.predict(X_test)
accuracy_rf = accuracy_score(y_test, y_pred_rf)
print(f'Random Forest Accuracy: {accuracy_rf:.2f}')

import matplotlib.pyplot as plt

# Get feature importance
importances = rf_model.feature_importances_
features = X.columns

# Plot
plt.bar(features, importances)
plt.xticks(rotation=90)
plt.title('Feature Importance')
plt.show()

from sklearn.metrics import confusion_matrix, ConfusionMatrixDisplay

# Plot confusion matrix
cm = confusion_matrix(y_test, y_pred_rf)
disp = ConfusionMatrixDisplay(confusion_matrix=cm)
disp.plot()
plt.show()