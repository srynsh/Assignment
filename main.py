import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

###
#### Surynansh Jain
#### cs21btech11057
###
# P7 b)

# i)

plt.annotate('A', xy=(0, 4), textcoords='data')
plt.annotate('B', xy=(2, 3), textcoords='data')
plt.annotate('C', xy=(1, 1), textcoords='data')
plt.annotate('D', xy=(2, 0), textcoords='data')

# ii)

plt.annotate('B\' (-2, 3)', xy=(-2, 3), textcoords='data')
plt.annotate('C\' (-1, 1)', xy=(-1, 1), textcoords='data')
plt.annotate('D\' (-2, 0)', xy=(-2, 0), textcoords='data')

# iii)

plt.plot([0, 2], [4, 3])  # Joining A to B
plt.plot([0, -2], [4, 3])  # Joining A to B'

plt.plot([2, 1], [3, 1])  # Joining B to C
plt.plot([-2, -1], [3, 1])  # Joining B' to C'

plt.plot([2, 1], [0, 1])  # Joining C to D
plt.plot([-2, -1], [0, 1])  # Joining C' to D'

plt.plot([2, -2], [0, 0])  # Joining D to D'

plt.plot([0, 0], [0, 5], label='Line of symmetry')  # Line of symmetry

plt.xlabel("x-axis")
plt.ylabel("Y-axis")

plt.legend()
plt.show()
