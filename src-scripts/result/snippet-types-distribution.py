import matplotlib.pyplot as plt
import numpy as np

labels = ['Java', 'Python', 'JavaScript']
java = [78.28, 82.18, 75.47]
python = [7.27, 7.03, 8.23]
js = [14.45, 8.23, 16.30]

x = np.arange(len(labels))  # the label locations
barWidth = 0.25  # the width of the bars
r1 = np.arange(len(labels))
r2 = [x + barWidth for x in r1]
r3 = [x + barWidth for x in r2]

fig, ax = plt.subplots()
# ax.set_ylim(100)
# ax.set_ybound(85)
# Make the plot
rects1 = ax.bar(r1, java, color='#7f3d5f', width=barWidth, edgecolor='white', label='Boiler-Plate')
rects2 = ax.bar(r2, python, color='#557f2d', width=barWidth, edgecolor='white', label='Fair')
rects3 = ax.bar(r3, js, color='#2d7f5e', width=barWidth, edgecolor='white', label='Good')

# Add some text for labels, title and custom x-axis tick labels, etc.
# ax.set_ylabel('percentage')
# ax.set_title('Scores by group and gender')
# ax.set_xticks([r + barWidth for r in range(len(java))], labels)
# ax.xticks([r + barWidth for r in range(len(java))], labels)
ax.set_xticks([0.25,1.25,2.25])
ax.set_xticklabels(labels)
ax.legend()


def autolabel(rects):
    """Attach a text label above each bar in *rects*, displaying its height."""
    for rect in rects:
        height = rect.get_height()
        ax.annotate('{}%'.format(height),
                    xy=(rect.get_x() + rect.get_width() / 2, height),
                    xytext=(0, 3),  # 3 points vertical offset
                    textcoords="offset points",
                    ha='center', va='bottom')


autolabel(rects1)
autolabel(rects2)
autolabel(rects3)

fig.tight_layout()
plt.savefig("snippet_category.png", dpi=150)
plt.show()
