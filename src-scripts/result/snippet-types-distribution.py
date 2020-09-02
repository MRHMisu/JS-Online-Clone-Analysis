# libraries
import matplotlib.pyplot as plt
import numpy as np

# set width of bar
barWidth = 0.35

# set height of bar
group = ['Java', 'Python', 'JavaScript']
bars1 = [78.28, 82.18, 75.47]
bars2 = [7.27, 7.03, 8.23]
bars3 = [14.45, 8.23, 16.30]

# Set position of bar on X axis
r1 = np.arange(len(bars1))
r2 = [x + barWidth for x in r1]
r3 = [x + barWidth for x in r2]

# Make the plot
plt.bar(r1, bars1, color='#7f6d5f', width=barWidth, edgecolor='white', label='Boiler-Plate (length <6)')
plt.bar(r2, bars2, color='#557f2d', width=barWidth, edgecolor='white', label='Fair ( 6 < length <10)')
plt.bar(r3, bars3, color='#2d7f5e', width=barWidth, edgecolor='white', label='Good ( 10<= length)')

# Add xticks on the middle of the group bars
# plt.xlabel('group', fontweight='bold')
plt.xticks([r + barWidth for r in range(len(bars1))], group)

# Create legend & Show graphic
plt.legend()
plt.show()
