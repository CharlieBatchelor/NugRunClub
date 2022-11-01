# =====================================================
# Code to plot 3 subplots, showing the average pace for
# each run of each person.

import pandas as pd
from matplotlib import pyplot as plt
import sys
import numpy as np

run = "Run"

fig, axs = plt.subplots(3, sharex=True, sharey=True)
fig.suptitle("Pace Analysis - < 5km, 5 - 10km, > 10km")
fig.supylabel("Minutes per km")

file_list = ['../activities/charlieActivities.csv', '../activities/matthewActivities.csv', '../activities/georgeActivities.csv',
             '../activities/rhysActivities.csv', "../activities/finchActivities.csv", "../activities/jennyActivities.csv"]
names = ["Charlie", "Matthew", "George", "Rhys", "Finch", "Jenny"]

for f, input_file in enumerate(file_list):
    activities = pd.read_csv(input_file, sep=',', header=0)

    paces1 = []  # < 5km
    paces2 = []  # 5 - 10km
    paces3 = []  # > 10km

    distances = activities["distance"]/1000
    movingTime = activities["moving_time"]/60
    type = activities["type"]
    
    for i in range(len(activities["distance"])):
        if activities["type"][i] == run:
            if distances[i] < 5 and movingTime[i] > 1:
                paces1.append(movingTime[i]/distances[i])
            if 5 <= distances[i] < 10:
                paces2.append(movingTime[i]/distances[i])
            if distances[i] >= 10:
                paces3.append(movingTime[i]/distances[i])

    # totalDistance = distances.sum()
    # totalTime = movingTime.sum()
    # averagePace = totalTime/totalDistance

    print("Number of paces: ", len(paces1), len(paces2), len(paces3))
    # 3 subplots for 5km, 10km, > 10km
    axs[0].plot(paces1, label=names[f])
    axs[0].set_title("Runs < 5km")
    axs[1].plot(paces2, label=names[f])
    axs[1].set_title("Runs 5 - 10km")
    axs[2].plot(paces3, label=names[f])
    axs[2].set_title("Runs > 10km")

    # plt.scatter(movingTime, distances, s=13, label=names[f])
    # plt.title("All Runs - Distance vs Time")
    # plt.ylabel("Distance (km)")
    # plt.xlabel("Time (minutes)")
    # plt.grid("both")

    # # New plot - all runs, distance vs elasped time
    # allDistances = data["distance"]/1000
    # allTimes = data["moving_time"]/60
    # print(len(allDistances))

    # # New plot - all runs, distance vs elasped time
    # allDistances = data["distance"]/1000
    # allTimes = data["moving_time"]/60
    # print(len(allDistances))

    # runs = []
    # time = []
    # run = "Run"
    # type = data["type"]
    #
    # # Only runs wanted!
    # for i in range(len(data)):
    #     if type[i] == run:
    #         runs.append(allDistances[i])
    #         time.append(allTimes[i])

plt.xlabel("Run #")
plt.xlim(-3, 30)
plt.legend()
plt.show()




