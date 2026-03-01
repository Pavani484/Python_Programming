import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score
import joblib

# Step 1: Data Collection (Load Sample Data)
data = pd.read_csv('mpce_data.csv')  # Replace with actual dataset

# Step 2: Data Preprocessing
data.dropna(inplace=True)  # Handling missing values
X = data.drop(columns=['MPCE'])  # Features
y = data['MPCE']  # Target variable

# Feature Scaling
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

# Step 3: Splitting Data into Training and Testing Sets
X_train, X_test, y_train, y_test = train_test_split(X_scaled, y, test_size=0.2, random_state=42)

# Step 4: Model Selection and Training
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

# Step 6: Deployment (Save Model)
joblib.dump(model, 'mpce_model.pkl')
joblib.dump(scaler, 'scaler.pkl')

# Step 7: Continuous Monitoring (Placeholder for Future Enhancements)
def predict_mpce(input_data):
    input_scaled = scaler.transform([input_data])
    return model.predict(input_scaled)[0]

# Example Usage
sample_input = X.iloc[0].values  # Replace with actual input
predicted_mpce = predict_mpce(sample_input)
print(f'Predicted MPCE: {predicted_mpce}')











