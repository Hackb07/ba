# Experiment 5: Data Preprocessing (Missing Values & Normalization)
# Aim: To perform data preprocessing operations including handling missing values and normalization.

import pandas as pd
from sklearn.preprocessing import MinMaxScaler

data = pd.DataFrame({
'Age':[22,25,None,28,30],
'Salary':[25000,30000,32000,None,40000]
})

# Handle missing values
data = data.fillna(data.mean())

print("After Handling Missing Values")
print(data)

# Normalization
scaler = MinMaxScaler()
scaled = scaler.fit_transform(data)

print("\nNormalized Data")
print(scaled)
