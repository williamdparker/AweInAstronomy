import numpy as np
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches

# Add data from SENS to nature_awe_responses
#   Make similar subplot for SENS data

# filename = 'AweInAstronomyClass.png'
filename = 'AweBeforeAstronomyClass.png'

plt.style.use('dark_background')
arrow_width = 0.5
arrow_color = 'lightgreen'
curve_width = 3.0
curve_color = 'lightpink'
text_color = 'white'
text_fontsize = 18
histogram_colormap = plt.cm.get_cmap('plasma')

figure, axes = plt.subplots()


nature_awe_responses = np.array([[3.2, 4.9, 3.8, 1.6, 2.3, 4.8, 3.2, 4.8, 3.0, 5.0, 3.6, 4.3, 4.2, 6.0, 5.6],
                                 [0.9, 0.9, 1.3, 1.6, 1.5, 2.2, 1.1, 0.9, 0.5, 1.3, 0.8, 0.7, 1.1, 1.2, 0.9j]])
class_awe_responses = np.array([[4.5, 5.3, 5.0, 4.6, 3.5, 3.5, 4.5, 3.5, 4.9, 4.5, 3.0, 3.5],
                                [1.7, 1.7, 1.1, 1.5, 1.4, 1.9, 0.8, 1.5, 1.8, 1.6, 1.3, 1.4]])

if filename == 'AweBeforeAstronomyClass.png':
    class_awe_responses = nature_awe_responses

bins = [1, 2, 3, 4, 5, 6, 7]

class_awe_average = np.average(class_awe_responses[0])
class_awe_standard_deviation = np.std(class_awe_responses[0])
peak_value = 6

normal_curve_input = np.linspace(bins[0], bins[-1])
normal_curve = peak_value * np.exp(-0.5 *
                                   np.power((normal_curve_input - class_awe_average)/class_awe_standard_deviation, 2)
                                   )

# Plot curve
plt.plot(normal_curve_input, normal_curve, linewidth=curve_width, color=curve_color)
# Plot linesegment at x = 4
plt.axvline(4, linestyle='dotted')

horizontal_range = bins[-1] - bins[0]
horizontal_midpoint = 0.5 * (bins[-1] + bins[0])
arrow_length = 0.4 * horizontal_range
left_arrow_start = 0.95 * horizontal_midpoint
right_arrow_start = 1.05 * horizontal_midpoint
arrow_vertical = -0.05 * peak_value
text_vertical = -0.15 * peak_value

# Add arrows
left_arrow = mpatches.Arrow(left_arrow_start, arrow_vertical, -arrow_length, 0.,
                            width=arrow_width, label='Disagree', color=arrow_color)
# axes.add_patch(left_arrow)
right_arrow = mpatches.Arrow(right_arrow_start, arrow_vertical, arrow_length, 0,
                             width=arrow_width, label='Agree', color=arrow_color)
# axes.add_patch(right_arrow)

# Label Likert scale
plt.text((1 - 0.37) * horizontal_midpoint, text_vertical, 'Disagree',
         ha='center', color=text_color, fontsize=text_fontsize)
plt.text((1 + 0.37) * horizontal_midpoint, text_vertical, 'Agree',
         ha='center', color=text_color, fontsize=text_fontsize)

plt.axis([bins[0], bins[-1], 0., peak_value + 1])
# Take the output of plt.hist as its components to manipulate later
number, bins, patches = plt.hist(class_awe_responses[0], bins=bins)

# Map bar center points to values between 0. and 1.
bin_centers = 0.5 * (bins[:-1] + bins[1:])
bar_colors = bin_centers - min(bin_centers)
bar_colors /= max(bar_colors)

for color, patch in zip(bar_colors, patches):
    # Set each bar's face color to the point along the colormap
    plt.setp(patch, 'facecolor', histogram_colormap(color))

plt.savefig(filename)
# plt.show()