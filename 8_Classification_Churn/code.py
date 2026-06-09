# Experiment 8: Classification Model (Customer Churn)
# Aim: To build a classification model using Logistic Regression.

import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression

data = pd.DataFrame({
'Usage':[10,20,30,40,50],
'Cost':[100,200,300,400,500],
'Churn':[0,0,1,1,1]
})

X = data[['Usage','Cost']]
y = data['Churn']

X_train,X_test,y_train,y_test = train_test_split(X,y,test_size=0.2)

model = LogisticRegression()
model.fit(X_train,y_train)

pred = model.predict(X_test)

print("Prediction:",pred)
