# Experiment 9: Customer Segmentation
# Aim: To segment customers based on purchase behavior using K-Means clustering.

import pandas as pd
from sklearn.cluster import KMeans

data = pd.DataFrame({
'Income':[15,16,17,40,42,44],
'Spending':[39,40,41,70,72,74]
})

kmeans = KMeans(n_clusters=2)
data['Cluster'] = kmeans.fit_predict(data)

print(data)
