import matplotlib.pyplot as plt
import numpy as np

# Data points for all clusters (green, red, blue)
data_points = {
    "Green": [(1, 2), (2, 3), (3, 3)],
    "Red": [(1, 2), (2, 3), (1, 4)],
    "Blue": [(3, 3), (5, 5), (4, 2)],
}

new_point = (2, 2)  # Point to classify

colors = {'Red': 'red', 'Blue': 'blue', 'Green': 'green'}

# Function to draw circle only for green cluster
def draw_circle(center, radius, color):
    circle = plt.Circle(center, radius, color=color, fill=False, linestyle="--", linewidth=1.5)
    plt.gca().add_patch(circle)

# Plot existing data points
plt.figure(figsize=(6, 6))

# Plot points for all clusters (red, blue, green)
for label, points in data_points.items():
    x_values, y_values = zip(*points)
    plt.scatter(x_values, y_values, color=colors[label], label=label, s=100)

    # For the green cluster, compute and draw the circle
    if label == "Green":
        # Compute cluster center (mean position of points in the class)
        center_x = np.mean(x_values)
        center_y = np.mean(y_values)
        center = (center_x, center_y)

        # Compute radius (maximum distance from center to a point in the cluster)
        radius = max(np.sqrt((np.array(x_values) - center_x) ** 2 + (np.array(y_values) - center_y) ** 2))

        # Draw circle for green points only
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
plt.title('Data Points with Green Circle Only')
plt.grid(True, linestyle="--", linewidth=0.5)
plt.legend()
plt.savefig('green_circle_only_plot.png', dpi=600)
plt.show()
