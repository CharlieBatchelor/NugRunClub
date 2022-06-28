# =====================================================
# Code to plot 3 subplots, showing the average pace for
# each run of each person.

import pandas as pd
from matplotlib import pyplot as plt
import sys
import numpy as np

run = "Run"
numRuns = 0
numEvents = 20

# Choose who you want
charlieActivities = pd.read_csv("charlieActivities.csv", sep=",", header=0)
charlieActivities = charlieActivities.head(numEvents)
matthewActivities = pd.read_csv("matthewActivities.csv", sep=",", header=0)
matthewActivities = matthewActivities.head(numEvents)
georgeActivities = pd.read_csv("georgeActivities.csv", sep=",", header=0)
georgeActivities = georgeActivities.head(numEvents)
rhysActivities = pd.read_csv("rhysActivities.csv", sep=",", header=0)
rhysActivities = rhysActivities.head(numEvents)
# activities = pd.read_csv("finchActivities.csv", sep=",", header=0)


charlie5paces = []
charlie10paces = []
charlie15paces = []

charlieDistances = charlieActivities["distance"]
charlieMovingTime = charlieActivities["moving_time"]

for i in range(len(charlieActivities["distance"])):
    if charlieActivities["type"][i] == run:
        if charlieDistances[i] <= 5000 and charlieMovingTime[i] > 100:
            charlie5paces.append(charlieDistances[i]/charlieMovingTime[i])
        if charlieDistances[i] > 5000 and charlieDistances[i] < 10000:
            charlie10paces.append(charlieDistances[i]/charlieMovingTime[i])
        if charlieDistances[i] >= 10000:
            charlie15paces.append(charlieDistances[i]/charlieMovingTime[i])

matthew5paces = []
matthew10paces = []
matthew15paces = []

matthewDistances = matthewActivities["distance"]
matthewMovingTime = matthewActivities["moving_time"]

for i in range(len(matthewActivities["distance"])):
    if matthewActivities["type"][i] == run:
        if matthewDistances[i] <= 5000 and matthewMovingTime[i] > 100:
            matthew5paces.append(matthewDistances[i]/matthewMovingTime[i])
        if matthewDistances[i] > 5000 and matthewDistances[i] < 10000:
            matthew10paces.append(matthewDistances[i]/matthewMovingTime[i])
        if matthewDistances[i] >= 10000:
            matthew15paces.append(matthewDistances[i]/matthewMovingTime[i])


rhys5paces = []
rhys10paces = []
rhys15paces = []

rhysDistances = rhysActivities["distance"]
rhysMovingTime = rhysActivities["moving_time"]

for i in range(len(rhysActivities["distance"])):
    if rhysActivities["type"][i] == run:
        if rhysDistances[i] <= 5000:
            rhys5paces.append(rhysDistances[i]/rhysMovingTime[i])
        if rhysDistances[i] > 5000 and rhysDistances[i] < 10000:
            rhys10paces.append(rhysDistances[i]/rhysMovingTime[i])
        if rhysDistances[i] >= 10000:
            rhys15paces.append(rhysDistances[i]/rhysMovingTime[i])

george5paces = []
george10paces = []
george15paces = []

georgeDistances = georgeActivities["distance"]
georgeMovingTime = georgeActivities["moving_time"]

for i in range(len(georgeActivities["distance"])):
    if georgeActivities["type"][i] == run:
        if georgeDistances[i] <= 5000:
            george5paces.append(georgeDistances[i]/georgeMovingTime[i])
        if georgeDistances[i] > 5000 and georgeDistances[i] < 10000:
            george10paces.append(georgeDistances[i]/georgeMovingTime[i])
        if georgeDistances[i] >= 10000:
            george15paces.append(georgeDistances[i]/georgeMovingTime[i])

# Average Pace All Time and All Distance
mattTotDis = matthewDistances.sum()/1000 # km
mattTotTime = matthewMovingTime.sum()/60 # min
mattPace = mattTotTime/mattTotDis

rhysTotDis = rhysDistances.sum()/1000
rhysTotTime = rhysMovingTime.sum()/60
rhysPace = rhysTotTime/rhysTotDis

georgeTotDis = georgeDistances.sum()/1000
georgeTotTime = georgeMovingTime.sum()/60
georgePace = georgeTotTime/georgeTotDis

print("All Time Pace Average (min/km)")
print("Matthew: ", mattPace)
print("Rhys: ", rhysPace)
print("George: ", georgePace)




# Plot the figure
fig, axs = plt.subplots(3)
# fig.suptitle("Pace Analysis - < 5km, 5 - 10km, > 10km")

# axs[0].plot(rhys5paces, 'r', label="Rhys", linewidth=2)
axs[0].plot(matthew5paces,'b', label="Matthew", linewidth=2)
# axs[0].plot(george5paces, 'gold', label="George", linewidth=2)
axs[0].plot(charlie5paces, 'purple', label="Charlie", linewidth=2)
axs[0].grid("both")
axs[0].set_ylabel("Pace (m/s)")
axs[0].legend(loc="lower right") # Add legend to top plot - less busy top right
axs[0].set_title("Runs < 5km")

# axs[1].plot(rhys10paces, 'r', label="Rhys", linewidth=2)
axs[1].plot(matthew10paces,'b', label="Matthew", linewidth=2)
# axs[1].plot(george10paces, 'gold', label="George", linewidth=2)
axs[1].plot(charlie10paces, 'purple', label="Charlie", linewidth=2)
axs[1].grid("both")
axs[1].set_title("Runs 5 - 10km")
axs[1].set_ylabel("Pace (m/s)")

# axs[2].plot(rhys15paces, 'r', label="Rhys", linewidth=2)
axs[2].plot(matthew15paces,'b', label="Matthew", linewidth=2)
# axs[2].plot(george15paces, 'gold', label="George", linewidth=2)
axs[2].plot(charlie15paces, 'purple', label="Charlie", linewidth=2)
axs[2].grid("both")
axs[2].set_title("Runs > 10km")
axs[2].set_ylabel("Pace (m/s)")
axs[2].set_xlabel("Run Number (Each Category)")

plt.show()




