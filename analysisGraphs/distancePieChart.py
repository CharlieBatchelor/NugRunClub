# =====================================================
# Analysis script, plots the normal pie chart!
import pandas as pd
from matplotlib import pyplot as plt
import sys
from datetime import datetime
import numpy as np

def create_pie_chart(values, labels, date):
    """
    Creates a nice Pie Chart of from two lists:
    :param values: The values to be represented by the chart.
    :param labels: The labels corresponding to each value
    :return: The plotted figure object.
    """
    # Create a figure and axis
    fig, ax = plt.subplots()

    # Set a modern style for the plot
    plt.style.use('seaborn-whitegrid')

    # Create the pie chart
    wedges, _, autotexts = ax.pie(values, labels=labels, autopct='%1.1f%%', startangle=90)

    # Set font size and color for the percentage labels
    for autotext in autotexts:
        autotext.set_fontsize(12)
        autotext.set_color('white')
        autotext.set_weight('bold')

    # Add a title
    ax.set_title(f'Nug Distance Contributions - {date}', fontweight='bold')

    # Equal aspect ratio ensures that pie is drawn as a circle
    ax.axis('equal')

    # Save chart to webserver area
    plt.savefig("website/frontend/images/pie.png")

    return fig

# date
now = datetime.now()
stringDate = now.strftime("%d-%m-%Y")
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

fig = create_pie_chart(distances, labels, stringDate)

plt.show()



