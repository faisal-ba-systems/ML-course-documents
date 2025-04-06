import matplotlib.pyplot as plt
import numpy as np
from matplotlib.patches import Circle

# Data points
data_points = np.array([(2, 3), (3, 4), (5, 8), (8, 8), (9, 10), (4, 5), (6, 4), (7, 5), (10, 2), (11, 3)])
x_values, y_values = data_points[:, 0], data_points[:, 1]

# Initial centroids
centroids = np.array([(2.5, 3.5), (4.5, 6.5), (8.5, 5.3)])

# Plotting data points
plt.figure(figsize=(8, 8))
plt.scatter(x_values, y_values, color='blue', s=100, label='Data Points')

# Plotting initial centroids
plt.scatter(centroids[0, 0], centroids[0, 1], color='red', s=150, marker='X', label='Centroid 1 (2.5,3.5)')
plt.scatter(centroids[1, 0], centroids[1, 1], color='green', s=150, marker='X', label='Centroid 2 (4.5,6.5)')
plt.scatter(centroids[2, 0], centroids[2, 1], color='purple', s=150, marker='X', label='Centroid 3 (8.5,5.3)')

# Drawing circles around centroids
radius = 2  # Arbitrary radius, adjust as needed
colors = ['red', 'green', 'purple']

for i, centroid in enumerate(centroids):
    circle = Circle((centroid[0], centroid[1]), radius, color=colors[i], fill=False, linestyle='--', linewidth=1.5)
    plt.gca().add_patch(circle)

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
plt.title('Centroids with Circles')
plt.legend()

plt.savefig('centroids_with_circles.png', dpi=600)
plt.show()
