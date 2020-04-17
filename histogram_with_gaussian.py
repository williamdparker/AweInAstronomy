import numpy as np
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches

# Add data from SENS to nature_awe_responses
#   Make similar subplot for SENS data
# Add Likert scale labels to x-axis

# Move arrows up and re-introduce labels

filename = 'AweInAstronomyClass.png'

plt.style.use('dark_background')
figure, axes = plt.subplots()


nature_awe_responses = np.array([[]])
class_awe_responses = np.array([[4.5, 5.3, 5.0, 4.6, 3.5, 3.5, 4.5, 3.5, 4.9, 4.5, 3.0, 3.5],
                                [1.7, 1.7, 1.1, 1.5, 1.4, 1.9, 0.8, 1.5, 1.8, 1.6, 1.3, 1.4]])

bins = [1, 2, 3, 4, 5, 6, 7]

class_awe_average = np.average(class_awe_responses[0])
class_awe_standard_deviation = np.std(class_awe_responses[0])
peak_value = 6

normal_curve_input = np.linspace(bins[0], bins[-1])
normal_curve = peak_value * np.exp(-0.5 *
                                   np.power((normal_curve_input - class_awe_average)/class_awe_standard_deviation, 2)
                                   )

plt.plot(normal_curve_input, normal_curve)

# Label Likert scale
#plt.text(2, -1.0, 'Disagree', ha='center')
#plt.text(6, -1.0, 'Agree', ha='center')

horizontal_range = bins[-1] - bins[0]
print(horizontal_range)
horizontal_midpoint = 0.5 * (bins[-1] + bins[0])
print(horizontal_midpoint)
arrow_length = 0.4 * horizontal_range
left_arrow_start = 0.95 * horizontal_midpoint
right_arrow_start = 1.05 * horizontal_midpoint
arrow_vertical = -0.5

# Add arrows
left_arrow = mpatches.Arrow(left_arrow_start, arrow_vertical, -arrow_length, 0.,
                            width=1.0, label='Disagree')
axes.add_patch(left_arrow)
right_arrow = mpatches.Arrow(right_arrow_start, arrow_vertical, arrow_length, 0,
                             width=1.0, label='Agree')
axes.add_patch(right_arrow)

plt.axis([bins[0], bins[-1], -0.9, peak_value + 1])
plt.hist(class_awe_responses[0], bins=bins)

# plt.savefig(filename)
plt.show()