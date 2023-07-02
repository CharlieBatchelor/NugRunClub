# =====================================================
# Analysis script, plots the normal pie chart and leader table
# from previous month.

import pandas as pd
from matplotlib import pyplot as plt
import sys
from datetime import datetime, timedelta
import numpy as np

def create_pie_chart(values, labels, date):
    """
    Creates a nice Pie Chart from two lists, ensuring matching values and labels.
    :param values: The values to be represented by the chart.
    :param labels: The labels corresponding to each value.
    :param date: The date for the chart title.
    :return: The plotted figure object.
    """
    if len(values) != len(labels):
        raise ValueError("Number of values and labels must be equal.")

    # Filter out zero or negative values and their corresponding labels
    filtered_values = []
    filtered_labels = []
    for val, lbl in zip(values, labels):
        if val > 0:
            filtered_values.append(val)
            filtered_labels.append(lbl)

    # Create a figure and axis
    fig, ax = plt.subplots()

    # Set a modern style for the plot
    plt.style.use('seaborn-whitegrid')

    # Create the pie chart
    wedges, _, autotexts = ax.pie(filtered_values, labels=filtered_labels, autopct='%1.1f%%', startangle=90)

    # Set font size and color for the percentage labels
    for autotext in autotexts:
        autotext.set_fontsize(12)
        autotext.set_color('white')
        autotext.set_weight('bold')

    # Add a title
    ax.set_title(f'Nug Distance Contributions - {date}', fontweight='bold')

    # Equal aspect ratio ensures that pie is drawn as a circle
    ax.axis('equal')

    # Save chart to the web server area
    plt.savefig("website/frontend/images/lastMonthsPie.png")

# read data
data = pd.read_csv("lastMonthsData.csv")
distances = data["Distance"].tolist()
names = data["Name"].tolist()
labels = []

#Get last months date:
current_date = datetime.now()
last_month_date = current_date - timedelta(days=current_date.day)
stringDate = last_month_date.strftime('%Y-%m')

# Make better labels:
for i, l in enumerate(names):
    d = round(distances[i], 2)
    labels.append(l + " " + str(d) + "km")

print(f"Distances: {distances}")
print(f"Names: {names}")
print(f"Labels: {labels}")

# Create and save the updated pie
create_pie_chart(distances, names, stringDate)