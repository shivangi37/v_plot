mport sys
from collections import defaultdict

freq_dict = defaultdict(lambda: defaultdict(int))

for line in sys.stdin:
    column = line.strip().split('\t')

    start_pos1 = int(column[2])
    end_pos1 = int(column[3])
    start_pos2 = int(column[8])
    end_pos2 = int(column[9])

    fragment_length = int(column[11])
    relative_position = ((start_pos2 + end_pos2) / 2) - ((start_pos1 + end_pos1) / 2)
    if -500 <= relative_position <= 500:
        freq_dict[relative_position][fragment_length] += 1




for relative_position, length in freq_dict.items():
    for fragment_length, frequency in length.items():
        print(f"{relative_position}\t{fragment_length}\t{frequency}")


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
plt()
