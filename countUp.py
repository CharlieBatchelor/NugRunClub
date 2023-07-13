# This script should read the downloaded strava data for everyone, the downloaded google sheet in as array,
# update my(all) bits and then save the new googleData.csv to be uploaded to google
import pandas as pd
from datetime import datetime

# My files to use when updating the google dataframe
file_list = ['charlieActivities.csv', 'matthewActivities.csv', 'georgeActivities.csv',
             'rhysActivities.csv', "finchActivities.csv"]

names = ["Charlie", "Matthew", "George", "Rhys", "Finch"]

all_avg_elevations = []
all_paces = []
all_tot_elevations = []
all_tot_10k = []
all_tot_5k = []
all_tot_2k = []
all_tot_distance = []

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

    all_tot_distance.append(tot_distance/1000)
    all_tot_2k.append(total_2k)
    all_tot_5k.append(total_5k)
    all_tot_10k.append(total_10k)
    all_tot_elevations.append(tot_el)
    all_paces.append(pace)
    all_avg_elevations.append(avg_el)

# Create a dictionary using the lists
data = {
    "Name": names,
    "Distance": all_tot_distance,
    "NumRuns2k": all_tot_2k,
    "NumRuns5k": all_tot_5k,
    "NumRuns10k": all_tot_10k,
    "TotalElevation": all_tot_elevations,
    "Pace": all_paces,
    "AvgElPerRun": all_avg_elevations
}

# Create the pandas DataFrame
googleData = pd.DataFrame(data)

# print(googleData.to_string())
googleData.to_csv("googleData.csv", index=False)



