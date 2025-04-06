import pandas as pd
import numpy as np  
# Iteratively update centroids until convergence
data_points = np.array([(2,3), (3,4), (5,8), (8,8), (9,10), (4,5), (6,4), (7,5), (10,2), (11,3)])


def k_means(data, initial_centroids, max_iterations=100):
    centroids = initial_centroids.copy()
    for _ in range(max_iterations):
        # Calculate distances to centroids
        distances = np.linalg.norm(data[:, np.newaxis] - centroids, axis=2)
        # Assign clusters
        cluster_assignments = np.argmin(distances, axis=1)
        # Compute new centroids
        new_centroids = np.array([data[cluster_assignments == k].mean(axis=0) for k in range(len(centroids))])
        # Check for convergence
        if np.allclose(centroids, new_centroids):
            break
        centroids = new_centroids
    return centroids, cluster_assignments + 1  # Adding 1 for cluster labeling

# Initial centroids
initial_centroids = np.array([(2, 3), (4, 5), (6, 4)])

# Run K-Means
final_centroids, final_cluster_assignments = k_means(data_points, initial_centroids)

# Prepare final result
final_result_df = pd.DataFrame({
    'Data Point': [f'({x},{y})' for x, y in data_points],
    'Final Cluster': final_cluster_assignments
})

final_centroids, final_result_df
print(final_centroids)
print(final_result_df)
final_result_df.to_csv('final_cluster_assignments.csv', index=False)
