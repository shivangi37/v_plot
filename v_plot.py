import sys
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



# Creating scatter plot
plt.figure(figsize=(8,6))
plt.scatter(x_values, y_values, c=color_values, cmap='twilight', s=10, marker='o') #setting the color map

# Adding labels and title
plt.xlabel('Position')
plt.ylabel('Length')
plt.title('V-plot')

# Step 5: Add color bar and grid
plt.colorbar(label='frequency') #color bar and grading varies according to frequency

# Display the plot
plt.grid(True)
plt.show()



