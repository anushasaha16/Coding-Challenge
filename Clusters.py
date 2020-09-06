#import libraries
import csv
import numpy as np
import pandas as pd
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt

#reads csv file into DataFrame
data = pd.read_csv('ClusterPlot.csv')

#set number of samples equal to the number of row labels of DataFrame
num_samples = len(data.index)


sum_of_squared_distances = []

#initializes the k-means and identifies the sum of squared distances for each k value
for k in range(1, num_samples):
    km = KMeans(n_clusters = k)
    km = km.fit(data)
    sum_of_squared_distances.append(km.inertia_)

#plots each k value to its inertia
plt.plot(range(1, num_samples), sum_of_squared_distances, '.-b')
plt.xlabel('k')
plt.ylabel('Sum of Squared Distances')
plt.title('Elbow Method For Optimal k')
plt.show()

#visualize data with 3 clusters
LABEL_COLOR_MAP = {0 : 'r', 1 : 'g', 2 : 'b'}
km = KMeans(n_clusters = 3)
km = km.fit(data)
label_color = [LABEL_COLOR_MAP[l] for l in km.labels_]
plt.scatter(data['V1'], data['V2'], c=label_color)
plt.show()







