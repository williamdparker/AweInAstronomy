import numpy as np
import matplotlib.pyplot as plt

nature_awe_responses = np.array([[]])
class_awe_responses = np.array([[4.5, 5.3, 5.0, 4.6, 3.5, 3.5, 4.5, 3.5, 4.9, 4.5, 3.0, 3.0, 3.5],
                                [1.7, 1.7, 1.1, 1.5, 1.4, 1.9, 0.8, 1.5, 1.8, 1.6, 1.3, 1.4]])

bins = [1, 2, 3, 4, 5, 6, 7]
number_of_bins = 6


class_awe_average = np.average(class_awe_responses[0])
class_awe_standard_deviation = np.std(class_awe_responses[0])
peak_value = 6

normal_curve_input = np.linspace(1, 7)
normal_curve = peak_value * np.exp(-0.5 * np.power((normal_curve_input - class_awe_average)/class_awe_standard_deviation, 2))

# (np.sqrt(2 * np.pi) * class_awe_standard_deviation)

plt.plot(normal_curve_input, normal_curve)

plt.axis([1, 7, 0, peak_value + 1])
plt.hist(class_awe_responses[0], bins=bins)
# plt.hist(class_awe_responses[0], bins=number_of_bins)
plt.show()