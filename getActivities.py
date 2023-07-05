print("Getting activities")
import requests
print("Got requests")
# import pandas
# print("Got pandas")
import pandas as pd
print("Got pandas again")
import json
print("Got JSON")
import csv
print("Got CSV")

print("Modules imported.")

jsons = ["tokens/charlieToken.json", "tokens/georgeToken.json", "tokens/matthewToken.json", "tokens/rhysToken.json", "tokens/finchToken.json", "tokens/jennyToken.json"]
csvs = ['charlieActivities.csv', 'georgeActivities.csv', 'matthewActivities.csv', 'rhysActivities.csv', "finchActivities.csv", "jennyActivities.csv"]

print("Getting activities")

for i, token in enumerate(jsons):
    print(f"Getting acts for {i}")
    # Get the tokens from file to connect to Strava
    with open(token) as json_file:
        strava_tokens = json.load(json_file)
        # Loop through all activities
        page = 1
        url = "https://www.strava.com/api/v3/activities"
        access_token = strava_tokens['access_token']
        print("Access token is: ", access_token, " person is: ", csvs[i])
        # Create the dataframe ready for the API call to store your activity data
        activities = pd.DataFrame(
            columns=[
                "id",
                "name",
                "start_date_local",
                "type",
                "distance",
                "moving_time",
                "elapsed_time",
                "total_elevation_gain",
                "end_latlng",
                "external_id"
            ]
        )
        while True:
            # get page of activities from Strava
            r = requests.get(url + '?access_token=' + access_token + '&per_page=200' + '&page=' + str(page))
            r = r.json()
            # if no results then exit loop
            if not r:
                break

            print(f"Results for {i} looks like: {r}")

            # otherwise add new data to dataframe
            for x in range(len(r)):
                activities.loc[x + (page - 1) * 200, 'id'] = r[x]['id']
                activities.loc[x + (page - 1) * 200, 'name'] = r[x]['name']
                activities.loc[x + (page - 1) * 200, 'start_date_local'] = r[x]['start_date_local']
                activities.loc[x + (page - 1) * 200, 'type'] = r[x]['type']
                activities.loc[x + (page - 1) * 200, 'distance'] = r[x]['distance']
                activities.loc[x + (page - 1) * 200, 'moving_time'] = r[x]['moving_time']
                activities.loc[x + (page - 1) * 200, 'elapsed_time'] = r[x]['elapsed_time']
                activities.loc[x + (page - 1) * 200, 'total_elevation_gain'] = r[x]['total_elevation_gain']
                activities.loc[x + (page - 1) * 200, 'end_latlng'] = r[x]['end_latlng']
                activities.loc[x + (page - 1) * 200, 'external_id'] = r[x]['external_id']
            # increment page
            page += 1

    activity_loc = "./activities/" + str(csvs[i])
    activities.to_csv(activity_loc)
