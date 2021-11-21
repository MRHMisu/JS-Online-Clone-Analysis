"""
Simple demo with multiple subplots.
"""
import matplotlib.pyplot as plt
from numpy import genfromtxt

java_data = genfromtxt('Java-Snippet-Frequency.csv', delimiter=',')
js_data = genfromtxt('JS-Snippet-Frequency.csv', delimiter=',')
python_data = genfromtxt('Python-Snippet-Frequency.csv', delimiter=',')

java_x = java_data[:, :-1]
java_y = java_data[:, -1]

js_x = js_data[:, :-1]
js_y = js_data[:, -1]

python_x = python_data[:, :-1]
python_y = python_data[:, -1]

fig = plt.figure(figsize=(18, 10))
fig.tight_layout()
# create a color palette
palette = plt.get_cmap('Set1')

plt.subplot(3, 3, 1)
plt.plot(java_x, java_y, marker='', color=palette(1), linewidth=1.9, alpha=0.9, label=1)
plt.yscale('log', basey=10)
plt.ylim((pow(10, 0), pow(10, 7)))
plt.xlim(-20,1500)
#plt.xticks([300,600,900,1200,1500])
plt.xlabel('Snippet length', fontsize=12, fontweight=0, color='black', style='oblique')
plt.ylabel('Frequency', fontsize=12, fontweight=0, color='black', style='oblique')
plt.title("Java", fontsize=12, fontweight=0, color='black', style='italic')

plt.subplot(3, 3, 2)
plt.plot(python_x, python_y, marker='', color=palette(2), linewidth=1.9, alpha=0.9, label=2)
plt.yscale('log', basey=10)
plt.ylim((pow(10, 0), pow(10, 7)))
plt.xlim(-20,1500)
plt.xlabel('Snippet length', fontsize=12, fontweight=0, color='black', style='oblique')
plt.ylabel('Frequency')
plt.title("Python", fontsize=12, fontweight=0, color='black', style='italic')

plt.subplot(3, 3, 3)
plt.plot(js_x, js_y, marker='', color=palette(3), linewidth=1.9, alpha=0.9, label=3)
plt.yscale('log', basey=10)
plt.ylim((pow(10, 0), pow(10, 7)))
plt.xlim(-20,1500)
plt.xlabel('Snippet length', fontsize=12, fontweight=0, color='black', style='oblique')
# plt.ylabel('Frequency')
plt.title("JavaScript", fontsize=12, fontweight=0, color='black', style='italic')

# plt.savefig("sample.png", dpi=150)
plt.show()
