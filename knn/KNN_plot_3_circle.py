import matplotlib.pyplot as plt
import numpy as np

# Given data points with class labels
data_points = {
     "Green": [(1,2), (2,3), (3,3)],
    "Red": [(1,2), (2,3), (1,4)],
    "Blue": [(3,3), (5,5), (4,2)],

}
new_point = (2,2)  # Point to classify

colors = {'Red': 'red', 'Blue': 'blue', 'Green': 'green'}

# Function to draw circles around clusters
def draw_circle(center, radius, color):
    circle = plt.Circle(center, radius, color=color, fill=False, linestyle="--", linewidth=1.5)
    plt.gca().add_patch(circle)

# Plot existing data points
plt.figure(figsize=(6,6))

for label, points in data_points.items():
    x_values, y_values = zip(*points)
    plt.scatter(x_values, y_values, color=colors[label], label=label, s=100)
    
    # Compute cluster center (mean position of points in the class)
    center_x = np.mean(x_values)
    center_y = np.mean(y_values)
    center = (center_x, center_y)
    
    # Compute radius (maximum distance from center to a point in the cluster)
    radius = max(np.sqrt((np.array(x_values) - center_x) ** 2 + (np.array(y_values) - center_y) ** 2))
    
    # Draw circle
    draw_circle(center, radius + 0.2, colors[label])

# Plot new point
plt.scatter(new_point[0], new_point[1], color='green', marker='*', s=200, label='New Point (2,2)')

# Label points
for label, points in data_points.items():
    for x, y in points:
        plt.text(x + 0.2, y, f'({x},{y})', fontsize=12)

plt.text(new_point[0] + 0.2, new_point[1], f'({new_point[0]},{new_point[1]})', fontsize=12, color='green')

# Setting axis limits and ticks
plt.xlim(0, 7)
plt.ylim(0, 7)
plt.xticks(range(0, 8, 1))
plt.yticks(range(0, 8, 1))

# Plot settings
plt.xlabel('X-axis')
plt.ylabel('Y-axis')
plt.title('KNN Data Points with Cluster Circles')
plt.grid(True, linestyle="--", linewidth=0.5)
plt.legend()
plt.savefig('KNN_centroids_new_vs_oldscatter_plot.png', dpi=600)
plt.show()