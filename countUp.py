# This script should read the downloaded strava data for everyone, the downloaded google sheet in as array,
# update my(all) bits and then save the new googleData.csv to be uploaded to google
import pandas as pd
from datetime import datetime

# My files to use when updating the google dataframe
file_list = ['charlieActivities.csv', 'matthewActivities.csv', 'georgeActivities.csv',
             'rhysActivities.csv', "finchActivities.csv", "jennyActivities.csv"]

names = ["Charlie", "Matthew", "George", "Rhys", "Finch", "Jenny"]

# Read google sheet data to a data frame
googleData = pd.read_csv("googleData.csv")
# Date Variable - eg 2022-02-01
now = datetime.now()
stringDate = now.strftime("%Y-%m")
print("String date: ", stringDate)
# stringDate = '2022-07' #artifici  al string to pull back month 2022-xx
run = "Run" # Run string to compare type later
group_pace = 0
group_pace_sum = 0
group_all_runs = 0

# loop over all input files and get data to right people
for i, input_file in enumerate(file_list):

    # get useful info and initialise variables for new person
    input_file = "./activities/" + str(input_file)
    data = pd.read_csv(input_file, sep=",", header=0)
    dis = data["distance"]
    type = data["type"]
    date = data["start_date_local"]
    elev = data["total_elevation_gain"]
    mov_t = data["moving_time"]
    no_acts = len(dis)  # Number of activities
    tot_distance = 0  # total distance for month
    tot_el = 0
    avg_pace_sum = 0
    all_runs = 0 # all runs, below 2km too for pace normalisation
    avg_el = 0
    total_2k = 0  # number of runs for month, above 2km!
    total_5k = 0
    total_10k = 0

    # Tally up the stuff we want to send to google doc
    for j in range(no_acts):
        start_date = date[j][0:7]
        # Make dis[j] > 2000 for the 2km condition
        if type[j] == run and start_date == stringDate and dis[j] != 0 and mov_t[j] != 0:
            tot_distance += dis[j]
            tot_el += elev[j]
            all_runs += 1
            avg_pace_sum += (mov_t[j])/(dis[j]/1000)

            if dis[j] >= 2000:
                total_2k += 1
            if dis[j] >= 5000:
                total_5k += 1
            if dis[j] >= 10000:
                total_10k += 1

        # Can only do average pace if there are some runs!
        if all_runs != 0:
            avg_pace = avg_pace_sum/all_runs
            group_pace_sum += avg_pace_sum
            group_all_runs += all_runs
            mins = avg_pace // 60
            secs = avg_pace % 60
            pace = str(int(mins)) + ":" + str(int(secs)).zfill(2)
            avg_el = tot_el/all_runs

        # print("Average pace of " + str(names[i]) + " is " + str(pace))

        if all_runs == 0:
            pace = str(0)

    for k, n in enumerate(googleData["Name"]):
        if n == names[i]:
            googleData.loc[k, "Distance"] = tot_distance/1000
            googleData.loc[k, "NumRuns2k"] = total_2k
            googleData.loc[k, "NumRuns5k"] = total_5k
            googleData.loc[k, "NumRuns10k"] = total_10k
            googleData.loc[k, "TotalElevation"] = tot_el
            googleData.loc[k, "AveragePace"] = pace
            googleData.loc[k, "AvgElPerRun"] = avg_el

print(googleData.to_string())
googleData.to_csv("googleData.csv", index=False)



