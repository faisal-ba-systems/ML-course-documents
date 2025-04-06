
import numpy as np
import pandas as pd

# Define data points and initial centroids
data_points = np.array([(2, 3), (3, 4), (5, 8), (8, 8), (9, 10), (4, 5), (6, 4), (7, 5), (10, 2), (11, 3)])
# centroids = np.array([(2, 3), (5, 8), (10, 2)])
# centroids = np.array([(2, 3), (4, 5), (6, 4)])
# centroids = np.array([(2.5, 3.5), (4.5, 6.5), (8.5, 5.5)])
centroids = np.array([(2.5, 3.5), (5.0, 5.5), (9.0, 5.5)])

# Calculate Euclidean distance and assign clusters
distances = np.zeros((len(data_points), len(centroids)))
for i, point in enumerate(data_points):
    for j, centroid in enumerate(centroids):
        distances[i, j] = np.linalg.norm(point - centroid)

# Assign each point to the nearest centroid
cluster_assignments = np.argmin(distances, axis=1) + 1  # Adding 1 to label clusters as 1, 2, 3

# Calculate new centroids by averaging the points in each cluster
new_centroids = np.array([
    data_points[cluster_assignments == 1].mean(axis=0),
    data_points[cluster_assignments == 2].mean(axis=0),
    data_points[cluster_assignments == 3].mean(axis=0)
])

# Display new centroids
print('new_centroids: \n',new_centroids)


# Create a DataFrame to display the results
df = pd.DataFrame({
    'Data Point': [f'({x},{y})' for x, y in data_points],
    'Distance to C1 (2,3)': distances[:, 0],
    'Distance to C2 (4,5)': distances[:, 1],
    'Distance to C3 (6,4)': distances[:, 2],
    'Assigned Cluster': cluster_assignments
})

df.to_csv('cluster_assignments.csv', index=False)
