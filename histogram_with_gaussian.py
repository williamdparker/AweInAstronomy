import numpy as np
import matplotlib.pyplot as plt

# Add data from SENS to nature_awe_responses
#   Make similar subplot for SENS data
# Add Likert scale labels to x-axis


nature_awe_responses = np.array([[]])
class_awe_responses = np.array([[4.5, 5.3, 5.0, 4.6, 3.5, 3.5, 4.5, 3.5, 4.9, 4.5, 3.0, 3.0, 3.5],
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

plt.axis([bins[0], bins[-1], 0, peak_value + 1])

plt.hist(class_awe_responses[0], bins=bins)

plt.show()