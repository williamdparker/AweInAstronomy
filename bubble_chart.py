import numpy as np
import matplotlib.pyplot as plt

# Bubble for awe in center at (0.5, 0.5)
# Six bubbles for each factor of awe arranged in symmetrical patter (regular hexagon) around center bubble)
# Bubble centers at:
#   Accomodation    5.0(5)  (horizontal_whitespace + diameter / 2,      0.5 - (diameter + length) / 2)
#   Physical        3.6(5)  (0.5,                                       vertical_whitespace + diameter / 2)
#   Vastness        5.0(5)  (1 - (horizontal_whitespace + diameter / 2),0.5 - (diameter + length / 2)
#   Connection      4.1(5)  (1 - (horizontal_whitespace + diameter / 2),0.5 + (diameter + length / 2)
#   Self-Loss       3.6(5)  (0.5,                                       1 - (vertical_whitespace + diameter / 2))
#   Time            4.1(3)  (horizontal_whitespace + diameter / 2,      0.5 + (diameter + length) / 2)

# plt.show()