# Experiment 3: Descriptive Statistics, Correlation Analysis and Predictive Model
# Aim: To perform descriptive statistics (mean, standard deviation, median) and correlation analysis,
# and build a predictive model using a dataset created as a Pandas DataFrame.

import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression

# Create DataFrame
data = pd.DataFrame({
    'feature1':[10,20,30,40,50],
    'feature2':[15,25,35,45,55],
    'target':[100,200,300,400,500]
})

# Descriptive statistics
print("Descriptive Statistics")
print(data.describe())

# Correlation
print("\nCorrelation Matrix")
print(data.corr())

# Predictive model
X = data[['feature1','feature2']]
y = data['target']

X_train,X_test,y_train,y_test = train_test_split(X,y,test_size=0.2)

model = LinearRegression()
model.fit(X_train,y_train)

pred = model.predict(X_test)
print("\nPredicted Value:",pred)
