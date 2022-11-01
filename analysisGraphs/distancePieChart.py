# =====================================================
# Analysis script, plots the normal pie chart!
import pandas as pd
from matplotlib import pyplot as plt
import sys
from datetime import datetime
import numpy as np


# date
now = datetime.now()
stringDate = now.strftime("%Y-%m")
# stringDate = "2022-07"

# I think paths have to be relative to the dataGrabber.sh script!
counted_data = np.genfromtxt("googleData.csv", delimiter=",")
counted_data = counted_data.transpose()

# Pie chart, where the slices will be ordered and plotted counter-clockwise:
distances = counted_data[1][1:]
distances = np.array(distances)
labels = ["George", "Rhys", "Charlie", "Matthew", "Finch"]

# Make better labels:
for i, l in enumerate(labels):
    d = round(distances[i], 2)
    labels[i] = l + " " + str(d) + "km"

explode = np.zeros(len(distances))
print(distances.argmax())
explode[distances.argmax()] = 0.1

fig1, ax1 = plt.subplots()
ax1.pie(distances, explode=explode, labels=labels, autopct='%1.1f%%',
        shadow=True, startangle=90,
        textprops={'color': 'black', 'weight': 'bold', 'fontsize': 10})
ax1.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.



# plt.savefig("website/frontend/images/pie.png")
