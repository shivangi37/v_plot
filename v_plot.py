import sys
import matplotlib.pyplot as plt
import numpy as np

# Define the matrix dimensions
x_min, x_max = -500, 500
y_min, y_max = 0, 500
rows = y_max - y_min + 1  # Number of rows (501)
cols = x_max - x_min + 1  # Number of columns (1001)

# Create a 2D matrix initialized to zero
frequency_matrix = np.zeros((rows, cols))

# Function to convert (x, y) coordinates to matrix indices
def to_matrix_indices(x, y):
    # Map x from [-500, 500] to [0, 1000] for columns
    col = x - x_min
    # Map y from [0, 500] to [0, 500] for rows
    row = y - y_min
    return row, col

# Function to count frequencies from example coordinates
def count_frequencies():
    # Example coordinates for frequency counting (replace this with your actual data)
    default_coordinates = [
        (-500, 0), (-400, 100), (0, 250), (200, 400), (500, 500),
        (-250, 250), (100, 100), (300, 450), (-100, 150), (0, 500),
        (-500, 500), (0, 0), (250, 250), (400, 0), (450, 200)
    ]

    for x, y in default_coordinates:
        # Make sure the coordinates are within bounds
        if x_min <= x <= x_max and y_min <= y <= y_max:
            # Get matrix indices for the coordinates
            row_idx, col_idx = to_matrix_indices(x, y)
            # Increment the corresponding cell in the matrix, scaling up to make points larger
            frequency_matrix[row_idx][col_idx] += 10  # Increase the scale factor to make the points stand out

# Count frequencies
count_frequencies()

# Create the heatmap
plt.figure(figsize=(15, 10))  # Increase the figure size for better visibility

# Set the background color to white
plt.gca().set_facecolor('white')
plt.gcf().patch.set_facecolor('white')  # Set the figure background to white

# Use the 'Blues' colormap for the background heatmap
plt.imshow(frequency_matrix, extent=[x_min, x_max, y_min, y_max], origin='lower', cmap='Blues', aspect='auto', interpolation='nearest')

# Overlay scatter plot with different colors based on frequency
y_indices, x_indices = np.nonzero(frequency_matrix)  # Get the indices where the frequency is non-zero
frequencies = frequency_matrix[y_indices, x_indices]  # Extract frequency values

# Create a colormap for scatter points based on frequency
scatter = plt.scatter(x_indices + x_min, y_indices + y_min, c=frequencies, s=500, cmap='viridis')

# Add colorbar for the scatter plot
cbar = plt.colorbar(scatter, label='Frequency', pad=0.01)
cbar.set_label('Frequency')

# Add contour lines for better visualization of the distribution
contours = plt.contour(frequency_matrix, levels=10, extent=[x_min, x_max, y_min, y_max], colors='black', linewidths=2)  # Add thicker contours
plt.clabel(contours, inline=True, fontsize=10, fmt='%.0f')  # Label contours

# Add titles and labels
plt.title('V PLOT GRAPH', fontsize=18)
plt.xlabel('X Coordinate', fontsize=14)
plt.ylabel('Y Coordinate', fontsize=14)

# Save the heatmap as an image with a white background
plt.savefig('v_plot_colored_frequency.png', bbox_inches='tight', facecolor='white', dpi=300)
plt.show()