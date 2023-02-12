# =====================================================
# Code to plot 3 subplots, showing the average pace for
# each run of each person.
import pandas as pd
from matplotlib import pyplot as plt
import sys
import numpy as np
from datetime import datetime, timedelta
from dateutil.relativedelta import *

# Variables
run = "Run"
numMonths = 12  # Number of months to go back

names = ["Charlie", "Matthew", "George", "Rhys", "Finch"]
file_list = ['../activities/charlieActivities.csv', '../activities/matthewActivities.csv', '../activities/georgeActivities.csv',
             '../activities/rhysActivities.csv', "../activities/finchActivities.csv"]

# Make a list of months that I can iterate through
now = datetime(datetime.now().year, datetime.now().month, 1)
then = (now + relativedelta(months=-numMonths))
months_list = []
while then <= now:
    then += timedelta(days=32) # This should shift us to the next month
    months_list.append(datetime(then.year, then.month, 1).strftime('%Y-%m'))

# Set up figure
fig = plt.subplot(111)
fig.set_title("Monthly Total Distances - Past 12 Months", fontweight="bold")
fig.set_ylabel("Total Distance Run (km)", fontweight="bold")
fig.set_xlabel("Month", fontweight="bold")

for f, file in enumerate(file_list):
    # Read the input file
    activities = pd.read_csv(file, sep=',', header=0)

    # Get relevant data
    distances = activities["distance"]
    movTimes = activities["moving_time"]
    date = activities["start_date_local"]
    type = activities["type"]
    monthly_totals = []

    # Now loop through the past 12 months, and all the activities of the current person
    for m, month in enumerate(months_list):
        total_distance = 0  # km
        for a in range(len(distances)):
            start_date = date[a][0:7]
            if type[a] == run and start_date == month and distances[a] != 0 and movTimes[a] != 0:
                total_distance += distances[a]/1000
        # Add the total distance run in that month to the totals list
        monthly_totals.append(total_distance)
        total_distance = 0

    plt.plot(months_list, monthly_totals, label=names[f], linewidth=3)

legend_properties = {'weight':'bold'}
plt.legend(prop=legend_properties)
plt.grid('both')
plt.show()




