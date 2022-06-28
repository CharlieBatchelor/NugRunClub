# This script should read the downloaded strava data for everyone, the downloaded google sheet in as array,
# update my(all) bits and then save the new googleData.csv to be uploaded to google
import pandas as pd
from matplotlib import pyplot as plt
import numpy as np
from datetime import datetime

# Date Variable
now = datetime.now()
stringDate = now.strftime("%Y-%m")
# Run string to compare type later
run = "Run"
# totalDistance variables

# # Read new csv files in - print current google data to terminal
# CHARLIE =======================================================
charlie = pd.read_csv("charlieActivities.csv", sep=",", header=0)
charlieDistance = charlie["distance"]
charlieExType = charlie["type"]
charlieDate = charlie["start_date_local"]
charlieNum = len(charlieDistance)
charlieTotDistance = 0

print("Calculating Charlie's Distance...")
for i in range(charlieNum):
    date = charlieDate[i][0:7] # correct date for comparison
    # If it's a run, and it's within the current month then count up
    if charlieExType[i] == run and date == stringDate:
        charlieTotDistance = charlieTotDistance + charlieDistance[i]
charlieTotDistance = charlieTotDistance/1000  # to km
print(charlieTotDistance)

# RHYS ==========================================================
rhys = pd.read_csv("rhysActivities.csv", sep=",", header=0)
rhysDistance = rhys["distance"]
rhysExType = rhys["type"]
rhysDate = rhys["start_date_local"]
rhysTotDistance = 0
rhysNum = len(rhysDistance)

print("Calculating Rhys's Distance...")

for i in range(rhysNum):
    date = rhysDate[i][0:7]  # correct date for comparison
    # If it's a run, and it's within the current month then count up
    if rhysExType[i] == run and date == stringDate:
        rhysTotDistance += rhysDistance[i]
rhysTotDistance = rhysTotDistance/1000  # to km
print(rhysTotDistance)

# GEORGE ========================================================
george = pd.read_csv("georgeActivities.csv", sep=",", header=0)
georgeDistance = george["distance"]
georgeExType = george["type"]
georgeDate = george["start_date_local"]
georgeTotDistance = 0
georgeNum = len(georgeDistance)

print("Calculating George's Distance...")
for i in range(georgeNum):
    date = georgeDate[i][0:7]  # correct date for comparison
    # If it's a run, and it's within the current month then count up
    if georgeExType[i] == run and date == stringDate:
        georgeTotDistance += georgeDistance[i]
georgeTotDistance = georgeTotDistance/1000  # to km
print(georgeTotDistance)

# MATTHEW ========================================================
matthew = pd.read_csv("matthewActivities.csv", sep=",", header=0)
matthewDistance = matthew["distance"]
matthewExType = matthew["type"]
matthewDate = matthew["start_date_local"]
matthewTotDistance = 0
matthewNum = len(matthewDistance)
print("Calculating Matthew's Distance...")

for i in range(matthewNum):
    date = matthewDate[i][0:7]  # correct date for comparison
    # If it's a run, and it's within the current month then count up
    if matthewExType[i] == run and date == stringDate:
        matthewTotDistance += matthewDistance[i]
matthewTotDistance = matthewTotDistance/1000  # to km
print(matthewTotDistance)

# FINCH ========================================================
# finch = pd.read_csv("finchActivities.csv", sep=",", header=0)
# finchDistance = finch["distance"]
# finchExType = finch["type"]
# finchDate = finch["start_date_local"]
# finchTotDistance = 0
# finchNum = len(finchDistance)
#
# print("Calculating Finch's Distance...")
#
# for i in range(matthewNum):
#     date = finchDate[i][0:7] # correct date for comparison
#     # If it's a run, and it's within the current month then count up
#     if finchExType[i] == run and date == stringDate:
#         finchTotDistance += finchDistance[i]
# finchTotDistance = finchTotDistance/1000  # to km
# print("Done: " + finchTotDistance)


googleData = pd.read_csv("googleData.csv")
print(googleData.to_string())

# Fill new googleData.csv file
distances = googleData["Distance"]
names = googleData["Name"]

# This is essentially code for a switch - probably could update this for efficiency later
for i in range(len(googleData["Name"])):
    if names[i] == "Charlie":
        distances[i] = charlieTotDistance
    if names[i] == "Rhys":
        distances[i] = rhysTotDistance
    if names[i] == "George":
        distances[i] = georgeTotDistance
    # if names[i] == "Finch":
    #     distances[i] = finchTotDistance
    if names[i] == "Matthew":
        distances[i] = matthewTotDistance

# Reprint updated data
print(googleData.to_string())
googleData.to_csv("googleData.csv", index=False)



