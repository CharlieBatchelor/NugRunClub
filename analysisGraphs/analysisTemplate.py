# =====================================================
# Analysis python script template.

import pandas as pd
from matplotlib import pyplot as plt
import sys
import numpy as np

walk = "Walk"
run = "Run"
numRuns = 0
numEvents = 20

# date
# now = datetime.now()
# stringDate = now.strftime("%Y-%m")
stringDate = "2022-01"

# Glob the files
file_list = ['../charlieActivities.csv', '../matthewActivities.csv', '../georgeActivities.csv', '../rhysActivities.csv', "../finchActivities.csv"]
names = ["charlie", "matthew", "george", "rhys", "finch"]
# Choose who you want
# charlieActivities = pd.read_csv("../charlieActivities.csv", sep=",", header=0)
# # charlieActivities = charlieActivities.head(numEvents)
# matthewActivities = pd.read_csv("../matthewActivities.csv", sep=",", header=0)
# # matthewActivities = matthewActivities.head(numEvents)
# georgeActivities = pd.read_csv("../georgeActivities.csv", sep=",", header=0)
# # georgeActivities = georgeActivities.head(numEvents)
# rhysActivities = pd.read_csv("../rhysActivities.csv", sep=",", header=0)
# # rhysActivities = rhysActivities.head(numEvents)
# finchActivities = pd.read_csv("../finchActivities.csv", sep=",", header=0)

# CHARLIE =============================================
charlieDistances = charlieActivities["distance"]
charlieMovingTime = charlieActivities["moving_time"]
charlieTotDistance = 0
charlieTotTime = 0
charlieRuns = 0
charlieDate = charlieActivities["start_date_local"]

if len(charlieDistances) != 0:
    for i in range(len(charlieActivities["distance"])):
        date = charlieDate[i][0:7]
        if charlieActivities["type"][i] == run and date == stringDate:
            charlieRuns += 1
            charlieTotDistance += charlieDistances[i]
            charlieTotTime += charlieMovingTime[i]

# RHYS =============================================
rhysDistances = rhysActivities["distance"]
rhysMovingTime = rhysActivities["moving_time"]
rhysTotDistance = 0
rhysTotTime = 0
rhysRuns = 0
rhysDate = rhysActivities["start_date_local"]

if len(charlieDistances) != 0:
    for i in range(len(rhysActivities["distance"])):
        date = rhysDate[i][0:7]
        if rhysActivities["type"][i] == run and date == stringDate:
            rhysRuns += 1
            rhysTotDistance += rhysDistances[i]
            rhysTotTime += rhysMovingTime[i]

# GEORGE =============================================
georgeDistances = georgeActivities["distance"]
georgeMovingTime = georgeActivities["moving_time"]
georgeTotDistance = 0
georgeTotTime = 0
georgeRuns = 0
georgeDate = georgeActivities["start_date_local"]

if len(georgeDistances) != 0:
    for i in range(len(georgeActivities["distance"])):
        date = georgeDate[i][0:7]
        if georgeActivities["type"][i] == run and date == stringDate:
            georgeRuns += 1
            georgeTotDistance += georgeDistances[i]
            georgeTotTime += georgeMovingTime[i]
# MATTHEW =============================================
matthewDistances = matthewActivities["distance"]
matthewMovingTime = matthewActivities["moving_time"]
matthewTotDistance = 0
matthewTotTime = 0
matthewRuns = 0
matthewDate = matthewActivities["start_date_local"]

if len(matthewDistances) != 0:
    for i in range(len(matthewActivities["distance"])):
        date = matthewDate[i][0:7]
        if matthewActivities["type"][i] == run and date == stringDate:
            matthewRuns += 1
            matthewTotDistance += matthewDistances[i]
            matthewTotTime += matthewMovingTime[i]


finchDistances = finchActivities["distance"]
finchMovingTime = finchActivities["moving_time"]
finchTotDistance = 0
finchTotTime = 0
finchRuns = 0
finchDate = finchActivities["start_date_local"]

if len(finchDistances) != 0:
    for i in range(len(finchActivities["distance"])):
        date = finchDate[i][0:7]
        if finchActivities["type"][i] == run and date == stringDate:
            finchRuns += 1
            finchTotDistance += finchDistances[i]
            finchTotTime += finchMovingTime[i]




print("\n          Total Distance (km) --- No. Runs --- Average Rune Distance (km)\n")
print("Charlie  ", charlieTotDistance/1000, "  ", charlieRuns, "  ", (charlieTotDistance/1000)/charlieRuns)
print("Rhys  ", rhysTotDistance/1000, "  ", rhysRuns, "  ", (rhysTotDistance/1000)/rhysRuns)
print("George  ", georgeTotDistance/1000, "  ", georgeRuns, "  ", (georgeTotDistance/1000)/georgeRuns)
print("Matthew  ", matthewTotDistance/1000, "  ", matthewRuns, "  ", (matthewTotDistance/1000)/matthewRuns)
print("Finch  ", finchTotDistance/1000, "  ", finchRuns, "  ", (finchTotDistance/1000)/finchRuns)
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


# plt.scatter(charlieMovingTime, charlieDistances, s=4, label="Charlie")
# plt.scatter(rhysMovingTime, rhysDistances, s=4, label="Rhys")
# plt.scatter(matthewMovingTime, matthewDistances, s=4, label="Matthew")
# plt.scatter(georgeMovingTime, georgeDistances,  s=4, label="George")
# plt.title("All Runs - Distance vs Time")
# plt.ylabel("Distance (m)")
# plt.legend()
# plt.xlabel("Time (sec)")
# plt.grid("both")
# plt.show()

# # Plot the figure
# fig, axs = plt.subplots(3)
# # fig.suptitle("Pace Analysis - < 5km, 5 - 10km, > 10km")
#
# axs[0].plot(rhys5paces, 'r', label="Rhys", linewidth=2)
# axs[0].plot(matthew5paces,'b', label="Matthew", linewidth=2)
# axs[0].plot(george5paces, 'gold', label="George", linewidth=2)
# axs[0].plot(charlie5paces, 'purple', label="Charlie", linewidth=2)
# axs[0].grid("both")
# axs[0].set_ylabel("Pace (m/s)")
# axs[0].legend(loc="lower right") # Add legend to top plot - less busy top right
# axs[0].set_title("Runs < 5km")
#
# axs[1].plot(rhys10paces, 'r', label="Rhys", linewidth=2)
# axs[1].plot(matthew10paces,'b', label="Matthew", linewidth=2)
# axs[1].plot(george10paces, 'gold', label="George", linewidth=2)
# axs[1].plot(charlie10paces, 'purple', label="Charlie", linewidth=2)
# axs[1].grid("both")
# axs[1].set_title("Runs 5 - 10km")
# axs[1].set_ylabel("Pace (m/s)")
#
# axs[2].plot(rhys15paces, 'r', label="Rhys", linewidth=2)
# axs[2].plot(matthew15paces,'b', label="Matthew", linewidth=2)
# axs[2].plot(george15paces, 'gold', label="George", linewidth=2)
# axs[2].plot(charlie15paces, 'purple', label="Charlie", linewidth=2)
# axs[2].grid("both")
# axs[2].set_title("Runs > 10km")
# axs[2].set_ylabel("Pace (m/s)")
# axs[2].set_xlabel("Run Number (Each Category)")
#
# plt.show()




