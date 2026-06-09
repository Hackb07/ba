# Experiment 7: Bivariate and Multivariate Analysis
# Aim: To perform bivariate and multivariate analysis using visualization techniques.

import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

data = pd.DataFrame({
'A':[1,2,3,4,5],
'B':[5,4,3,2,1],
'C':[2,3,4,5,6]
})

# Bivariate
sns.scatterplot(x='A',y='B',data=data)
plt.show()

# Multivariate
sns.pairplot(data)
plt.show()
