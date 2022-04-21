from scipy.spatial import Voronoi, voronoi_plot_2d
import numpy as np

points = np.genfromtxt("data.csv", delimiter=", ", usecols=(1,0))
names = np.genfromtxt("data-names.csv", delimiter="\n", dtype=str)
print(names)
points = np.append(points, [[9999,9999], [-9999,9999], [9999,-9999], [-9999,-9999]], axis = 0)

vor = Voronoi(points)

import matplotlib.pyplot as plt
fig, ax = plt.subplots(1, 1)
fig = voronoi_plot_2d(vor, ax, line_alpha=0.2)


# mapper = cm.ScalarMappable(norm=, cmap=cm.Blues_r)

labels = np.array([2,2,1,4,0,0,2,2,1,3])

for r in range(len(vor.point_region)):
    region = vor.regions[vor.point_region[r]]
    if not -1 in region:
        polygon = [vor.vertices[i] for i in region]
        plt.fill(*zip(*polygon), color=np.where(r<10, [1, 0.8, 0.8], [0.8, 1, 0.8]))
        x, y = vor.points[r]
        if r < 10:
            plt.text(x, y + 0.1, labels[r], va="bottom", ha="center")
        plt.text(x, y - 0.1, names[r], va="top", ha="center", fontsize=6)
plt.ylim([37,41]), plt.xlim([-109,-102])
plt.show()