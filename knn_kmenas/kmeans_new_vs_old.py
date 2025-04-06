import matplotlib.pyplot as plt
import numpy as np

# Data points
data_points = np.array([(2,3), (3,4), (5,8), (8,8), (9,10), (4,5), (6,4), (7,5), (10,2), (11,3)])
x_values, y_values = data_points[:, 0], data_points[:, 1]

# Initial old_centroids
# old_centroids = np.array([(2, 3), (4, 5), (6, 4)])
# old_centroids = np.array([(2.5, 3.5), (4.5, 6.5), (8.5, 5.5)])
old_centroids = np.array([(2.5, 3.5), (5.0, 5.5), (9.0, 5.5)])

new_centroids = np.array([(2.5, 3.5), (5.5, 5.5), (9.5, 5.75)])

# Plotting data points
plt.figure(figsize=(8, 8))
plt.scatter(x_values, y_values, color='blue', s=100, label='Data Points')

# Plotting initial old_centroids
plt.scatter(old_centroids[0, 0], old_centroids[0, 1], color='red', s=150, marker='X', label='Old Centroid 1 (2.5,3.5)')
plt.scatter(old_centroids[1, 0], old_centroids[1, 1], color='green', s=150, marker='X', label='Old Centroid 2 (5.0,5.5)')
plt.scatter(old_centroids[2, 0], old_centroids[2, 1], color='purple', s=150, marker='X', label='Old Centroid 3 (9.0,5.5)')

# Plotting initial old_centroids
plt.scatter(new_centroids[0, 0], new_centroids[0, 1], color='red', s=150, marker='*', label='New Centroid 1 (2.5,3.5)')
plt.scatter(new_centroids[1, 0], new_centroids[1, 1], color='green', s=150, marker='*', label='New Centroid 2 (5.5,5.5)')
plt.scatter(new_centroids[2, 0], new_centroids[2, 1], color='purple', s=150, marker='*', label='New Centroid 3 (9.5,5.75)')

# Labeling data points
for (x, y) in data_points:
    plt.text(x + 0.2, y, f'({x},{y})', fontsize=10)

# Setting axis limits and ticks
plt.xlim(0, 15)
plt.ylim(0, 15)
plt.xticks(range(0, 16, 1))
plt.yticks(range(0, 16, 1))

# Adding grid, labels, and title
plt.grid(True, linestyle="--", linewidth=0.5)
plt.xlabel('X-axis')
plt.ylabel('Y-axis')
plt.title('Centroids Update Scatter Plot')
plt.legend()
plt.savefig('centroids_new_vs_oldscatter_plot.png', dpi=600)
plt.show()
