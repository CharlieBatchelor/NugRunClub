# =====================================================
# Analysis python script template.

import pandas as pd
from matplotlib import pyplot as plt
import sys
import numpy as np
from datetime import datetime

walk = "Walk"
run = "Run"
numRuns = 0
numEvents = 20

# date
# now = datetime.now()
# stringDate = now.strftime("%Y-%m")
# stringDate = "2022-01"
now = datetime.now()
stringDate = now.strftime("%Y-%m")
print("Date: ", stringDate)

# Glob the files
file_list = ['../activities/charlieActivities.csv', '../activities/matthewActivities.csv', '../activities/georgeActivities.csv', '../activities/rhysActivities.csv', "../activities/finchActivities.csv", "../activities/jennyActivities.csv"]
names = ["charlie", "matthew", "george", "rhys", "finch", "jenny"]
months = ["2022-01","2022-02","2022-03","2022-04","2022-05","2022-06","2022-07","2022-08","2022-09","2022-10","2022-11"]

# CHARLIE =============================================
# charlieDistances = charlieActivities["distance"]
# charlieMovingTime = charlieActivities["moving_time"]
# charlieTotDistance = 0
# charlieTotTime = 0
# charlieRuns = 0
# charlieDate = charlieActivities["start_date_local"]
#
# if len(charlieDistances) != 0:
#     for i in range(len(charlieActivities["distance"])):
#         date = charlieDate[i][0:7]
#         if charlieActivities["type"][i] == run and date == stringDate:
#             charlieRuns += 1
#             charlieTotDistance += charlieDistances[i]
#             charlieTotTime += charlieMovingTime[i]
#
# # RHYS =============================================
# rhysDistances = rhysActivities["distance"]
# rhysMovingTime = rhysActivities["moving_time"]
# rhysTotDistance = 0
# rhysTotTime = 0
# rhysRuns = 0
# rhysDate = rhysActivities["start_date_local"]
#
# if len(charlieDistances) != 0:
#     for i in range(len(rhysActivities["distance"])):
#         date = rhysDate[i][0:7]
#         if rhysActivities["type"][i] == run and date == stringDate:
#             rhysRuns += 1
#             rhysTotDistance += rhysDistances[i]
#             rhysTotTime += rhysMovingTime[i]
#
# # GEORGE =============================================
# georgeDistances = georgeActivities["distance"]
# georgeMovingTime = georgeActivities["moving_time"]
# georgeTotDistance = 0
# georgeTotTime = 0
# georgeRuns = 0
# georgeDate = georgeActivities["start_date_local"]
#
# if len(georgeDistances) != 0:
#     for i in range(len(georgeActivities["distance"])):
#         date = georgeDate[i][0:7]
#         if georgeActivities["type"][i] == run and date == stringDate:
#             georgeRuns += 1
#             georgeTotDistance += georgeDistances[i]
#             georgeTotTime += georgeMovingTime[i]
# # MATTHEW =============================================
# matthewDistances = matthewActivities["distance"]
# matthewMovingTime = matthewActivities["moving_time"]
# matthewTotDistance = 0
# matthewTotTime = 0
# matthewRuns = 0
# matthewDate = matthewActivities["start_date_local"]
#
# if len(matthewDistances) != 0:
#     for i in range(len(matthewActivities["distance"])):
#         date = matthewDate[i][0:7]
#         if matthewActivities["type"][i] == run and date == stringDate:
#             matthewRuns += 1
#             matthewTotDistance += matthewDistances[i]
#             matthewTotTime += matthewMovingTime[i]
#
#
# finchDistances = finchActivities["distance"]
# finchMovingTime = finchActivities["moving_time"]
# finchTotDistance = 0
# finchTotTime = 0
# finchRuns = 0
# finchDate = finchActivities["start_date_local"]
#
# if len(finchDistances) != 0:
#     for i in range(len(finchActivities["distance"])):
#         date = finchDate[i][0:7]
#         if finchActivities["type"][i] == run and date == stringDate:
#             finchRuns += 1
#             finchTotDistance += finchDistances[i]
#             finchTotTime += finchMovingTime[i]

monthly_group_totals = []  # whole group total kms for month
monthly_indy_totals = []  # to show relative effort among the group
monthly_total = 0

for m in months:
    monthly_total = 0
    print("Analysing new month: ", m)
    for i, f in enumerate(file_list):

        # get activities of person
        acts = pd.read_csv(f, sep=",", header=0)
        distances = acts["distance"]
        moving_time = acts["moving_time"]
        totDis = 0
        totTime = 0
        date = acts["start_date_local"]

        for a in range(len(acts)):
            d = date[a][0:7]
            if acts["type"][a] == run and d == m:
                monthly_total += distances[a]/1000

    monthly_group_totals.append(monthly_total)

for i, f in enumerate(file_list):
    indy_total = 0
    list = []
    for m in months:
        # get activities of person
        acts = pd.read_csv(f, sep=",", header=0)
        distances = acts["distance"]
        moving_time = acts["moving_time"]
        totDis = 0
        totTime = 0
        date = acts["start_date_local"]

        for a in range(len(acts)):
            d = date[a][0:7]
            if acts["type"][a] == run and d == m:
                indy_total += distances[a]/1000
        list.append(indy_total)
        # print("Indy total: ", str(f), " is ", indy_total)
        indy_total = 0
    monthly_indy_totals.append(list)

print("Got ", len(monthly_indy_totals), " indy total lists.")
for l in monthly_indy_totals:
    monthly_group_totals.append(l)


print("Length of whole list: ", len(monthly_group_totals))

plt.xlabel("Month of 2022")
plt.ylabel("Total Distance (km)")

# plt.show()




