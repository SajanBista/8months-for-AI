import matplotlib.pyplot as plt
import numpy as np
from scipy.cluster.hierarchy import dendrogram, linkage

# Example dataset: [Annual Income, Spending Score]
data = np.array([
    [15, 39],  # Customer A
    [16, 81],  # Customer B
    [17, 6],   # Customer C
    [18, 77],  # Customer D
    [19, 40]   # Customer E
])

# Perform hierarchical/agglomerative clustering
linked = linkage(data, method='ward')

# Plot dendrogram
plt.figure(figsize=(8, 5))
dendrogram(linked,
           labels=['A', 'B', 'C', 'D', 'E'],
           distance_sort='ascending',
           show_leaf_counts=True)
plt.title('Dendrogram - Agglomerative Hierarchical Clustering')
plt.xlabel('Customer')
plt.ylabel('Euclidean Distance')
plt.grid(True)
plt.tight_layout()
plt.show()
