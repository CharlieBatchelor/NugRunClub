import requests
from pandas import json_normalize
import pandas as pd
import json
import csv

# Get the tokens from file to connect to Strava
with open("charlieToken.json") as json_file:
    strava_tokens = json.load(json_file)
    # Loop through all activities
    page = 1
    url = "https://www.strava.com/api/v3/activities"
    access_token = strava_tokens['access_token']
    print(access_token)
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
            "total_elevation_gain"
        ]
        )

    while True:
        # get page of activities from Strava
        r = requests.get(url + '?access_token=' + access_token + '&per_page=200' + '&page=' + str(page))
        r = r.json()
        # if no results then exit loop
        if not r:
            break

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

page += 1
activities.to_csv("charlieActivities.csv")
