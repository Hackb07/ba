# Experiment 10: Employee Attrition Prediction
# Aim: To predict whether an employee will leave the company using Decision Tree classification.

import pandas as pd
from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import train_test_split

data = pd.DataFrame({
'Age':[25,30,35,40,45],
'Salary':[30000,40000,50000,60000,70000],
'Attrition':[0,0,1,1,1]
})

X = data[['Age','Salary']]
y = data['Attrition']

X_train,X_test,y_train,y_test = train_test_split(X,y,test_size=0.2)

model = DecisionTreeClassifier()
model.fit(X_train,y_train)

pred = model.predict(X_test)

print("Prediction:",pred)
