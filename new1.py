import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler, LabelEncoder
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score
import joblib

# Step 1: Load Dataset
#data = pd.read_csv('mpce_data.csv')  # Ensure the dataset is available
data = pd.read_csv(r"D:/pydev/mpce_data.csv")

# Step 2: Data Preprocessing
# Handle missing values
data.dropna(inplace=True)

# Encode categorical features (if any)
categorical_cols = data.select_dtypes(include=['object']).columns
le = LabelEncoder()
for col in categorical_cols:
    data[col] = le.fit_transform(data[col])

# Split into features (X) and target (y)
X = data.drop(columns=['MPCE'])  # Features
y = data['MPCE']  # Target variable

# Feature Scaling
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

# Step 3: Split Data
#X_train, X_test, y_train, y_test = train_test_split(X_scaled, y, test_size=0.2, random_state=42)
X_train, X_test, y_train, y_test = train_test_split(X_scaled, y, test_size=0.3, random_state=42)

# Step 4: Train Model
model = RandomForestRegressor(n_estimators=100, random_state=42)
model.fit(X_train, y_train)

# Step 5: Model Evaluation
y_pred = model.predict(X_test)
mae = mean_absolute_error(y_test, y_pred)
mse = mean_squared_error(y_test, y_pred)
rmse = np.sqrt(mse)
r2 = r2_score(y_test, y_pred)

print(f'MAE: {mae}')
print(f'RMSE: {rmse}')
print(f'R² Score: {r2}')

# Step 6: Save Model
joblib.dump(model, 'mpce_model.pkl')
joblib.dump(scaler, 'scaler.pkl')

# Step 7: Prediction Function
def predict_mpce(input_data):
    input_scaled = scaler.transform([input_data])
    return model.predict(input_scaled)[0]

# Example Usage
sample_input = X.iloc[0].values  # Replace with actual input
predicted_mpce = predict_mpce(sample_input)
print(f'Predicted MPCE: {predicted_mpce}')


