import numpy as np
import matplotlib.pyplot as plt

# To-do:
#   Add colormap bar with Likert scale indicated
#   Make fonts nicer
#   Fix line segment length
#   Determine actual conversion factor between points and plot range
#   Figure out how to make transparent background

filename = 'FactorsOfAwe.png'

center_text = 'Factors\nof\nAwe'
factors_of_awe = ['Accommodation', 'Physical', 'Vastness', 'Connection', 'Self-Loss', 'Time']
factors_of_awe_survey_result_means = [5.0, 3.6, 5.0, 4.1, 3.6, 4.1]
factors_of_awe_survey_result_standard_deviations = [0.5, 0.5, 0.5, 0.5, 0.5, 0.3]
factors_of_awe_strings = []

for index in range(len(factors_of_awe)):
    factors_of_awe_strings.append(factors_of_awe[index] + '\n' + \
                                  str(factors_of_awe_survey_result_means[index]))

# + ' (' + \
# str(factors_of_awe_survey_result_standard_deviations[index]) + ')')

# Plot parameters
centertext_fontsize = 18
bubbletext_fontsize = int(0.75 * centertext_fontsize)
bubble_diameter = 2.5
bubble_colormap = 'plasma'
side_length = 3.0
points_per_plot_range = 40
bubble_transparency = 0.5
margin_size = 0.2

# Plot calculated parameters
number_of_vertices = len(factors_of_awe)
bubble_radius = bubble_diameter / 2.
intervertex_angle = 2 * np.pi / number_of_vertices
white_space = bubble_diameter
plot_range = 2 * bubble_radius + side_length + 2 * side_length * np.cos(intervertex_angle) + 2 * white_space
bubble_area = np.pi * (points_per_plot_range * bubble_radius) ** 2  # points ** 2
bubble_colors = factors_of_awe_survey_result_means

# Coordinates of bubbles at vertices of a regular polygon
polygon_point_indices = np.arange(0, number_of_vertices)
polygon_center = np.array([0.5*plot_range, 0.5*plot_range])
horizontal_coordinates = side_length * np.cos(polygon_point_indices * intervertex_angle) + polygon_center[0]
vertical_coordinates = side_length * np.sin(polygon_point_indices * intervertex_angle) + polygon_center[1]

# Coordinates of line segments run from central circle to vertices of regular polygon
line_starting_horizontal_coordinates = bubble_radius * np.cos(polygon_point_indices * intervertex_angle) + \
                                       polygon_center[0]
line_starting_vertical_coordinates = bubble_radius * np.sin(polygon_point_indices * intervertex_angle) + \
                                     polygon_center[1]
line_ending_horizontal_coordinates = (side_length - bubble_radius) * \
                                     np.cos(polygon_point_indices * intervertex_angle) + \
                                     polygon_center[0]
line_ending_vertical_coordinates = (side_length - bubble_radius) * \
                                   np.sin(polygon_point_indices * intervertex_angle) + \
                                   polygon_center[1]

# Plot line segments and text of bubbles
for index in polygon_point_indices:
    plt.plot(np.array([line_starting_horizontal_coordinates[index], line_ending_horizontal_coordinates[index]]),
             np.array([line_starting_vertical_coordinates[index], line_ending_vertical_coordinates[index]]),
             color='black', linewidth=4)
    plt.text(horizontal_coordinates[index], vertical_coordinates[index], factors_of_awe_strings[index],
             ha='center', va='center', fontsize=bubbletext_fontsize)

# Plot central text
plt.text(polygon_center[0], polygon_center[1], center_text, ha='center', va='center', fontsize=centertext_fontsize)

# Set axis range and turn off visualization of axis
#plt.axis([0., plot_range, 0., plot_range])
# plt.axis('equal', adjustable='box')
# plt.axis('square')
plt.axis('off')
plt.margins(margin_size)

# Plot bubbles
plt.scatter(horizontal_coordinates, vertical_coordinates, s=bubble_area, c=bubble_colors, alpha=bubble_transparency,
            cmap=bubble_colormap)
#plt.show()
plt.savefig(filename)