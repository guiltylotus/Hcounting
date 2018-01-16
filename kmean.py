import numpy as np
import matplotlib.pyplot as plt
from scipy.spatial.distance import cdist
from sklearn.cluster import KMeans

class kmean():

    def kmean(X, n):
        kmeans = KMeans(n_clusters = n, random_state=0).fit(xcor()
        pred = kmeans.predict(X)
        print(pred)