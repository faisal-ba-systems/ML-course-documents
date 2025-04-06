import matplotlib.pyplot as plt

# Data points
# data_points = [(2, 3), (3, 4), (8, 7), (9, 8)]
data_points = [(1, 2), (3, 4), (8, 7), (9, 8)]
x_values, y_values = zip(*data_points)

# Cluster centers
cluster_centers = [(2.5, 3.5), (8.5, 7.5)]
center_colors = ['red', 'green']

# Circle radius (adjust as needed)
radius = 2

# Plot the points
plt.figure(figsize=(6, 6))
plt.scatter(x_values, y_values, color='blue', label='Data Points', s=100)

# Label points
for i, (x, y) in enumerate(data_points):
    plt.text(x + 0.2, y, f'({x},{y})', fontsize=12)

# Plot cluster centers with circles
for (cx, cy), color in zip(cluster_centers, center_colors):
    plt.scatter(cx, cy, color=color, marker='X', s=200, label=f'Cluster Center ({cx},{cy})')
    
    # Add a circle around the centroid
    circle = plt.Circle((cx, cy), radius, color=color, fill=False, linestyle='--', linewidth=2)
    plt.gca().add_patch(circle)

# Setting axis limits and ticks
plt.xlim(0, 12)
plt.ylim(0, 12)
plt.xticks(range(0, 12, 1))
plt.yticks(range(0, 12, 1))

# Plot settings
plt.xlabel('X-axis')
plt.ylabel('Y-axis')
plt.title('Scatter Plot with Cluster Centers and Circles')
plt.grid(True, linestyle="--", linewidth=0.5)
plt.legend()
plt.show()
