# Experiment 6: Dimensionality Reduction using PCA, KPCA and SVD
# Aim: To perform dimensionality reduction using PCA, Kernel PCA, and SVD.

import pandas as pd
from sklearn.decomposition import PCA, KernelPCA, TruncatedSVD

data = pd.DataFrame({
'X1':[1,2,3,4,5],
'X2':[2,3,4,5,6],
'X3':[5,4,3,2,1]
})

# PCA
pca = PCA(n_components=2)
pca_result = pca.fit_transform(data)

# KPCA
kpca = KernelPCA(n_components=2,kernel='rbf')
kpca_result = kpca.fit_transform(data)

# SVD
svd = TruncatedSVD(n_components=2)
svd_result = svd.fit_transform(data)

print("PCA Result\n",pca_result)
print("\nKPCA Result\n",kpca_result)
print("\nSVD Result\n",svd_result)
