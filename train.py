import pandas as pd
from sklearn.ensemble import RandomForestClassifier
import pickle

print("1. Loading raw agricultural data...")
# Read the dataset
df = pd.read_csv('Data/crop_recommendation.csv')

# Extract the 7 input features
X = df[['N', 'P', 'K', 'temperature', 'humidity', 'ph', 'rainfall']]

# Extract the output (the crop name). If the column is named 'label', use it. Otherwise grab the last column.
y = df['label'] if 'label' in df.columns else df.iloc[:, -1]

print("2. Training the modern AI Model (Random Forest)...")
model = RandomForestClassifier(n_estimators=100, random_state=42)
model.fit(X, y)

print("3. Saving the new modern brain...")
# This overwrites the old, broken file with your new, modern one
pickle.dump(model, open('Crop_Recommendation2.pkl', 'wb'))

print("✅ Success! The new Crop_Recommendation2.pkl is ready.")