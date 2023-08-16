import requests
import pandas as pd
import json

jsons = ["tokens/charlieToken.json", "tokens/georgeToken.json", "tokens/matthewToken.json", "tokens/rhysToken.json", "tokens/finchToken.json"]
csvs = ['charlieActivities.csv', 'georgeActivities.csv', 'matthewActivities.csv', 'rhysActivities.csv', "finchActivities.csv"]

print("Getting activities")

for i, token in enumerate(jsons):
    print(f"Getting acts {csvs[i]}")
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
            r = requests.get(url + '?access_token=' + access_token + '&per_page=200' + '&page=' + str(page))
            r = r.json()
            if not r:
                break

            # Calculate the starting index for the current page
            start_index = (page - 1) * 200

            print(f"r looks like {r}")

            for x in range(len(r)):
                current_index = start_index + x
                activities.loc[current_index, 'id'] = r[x]['id']
                activities.loc[current_index, 'name'] = r[x]['name']
                activities.loc[current_index, 'start_date_local'] = r[x]['start_date_local']
                activities.loc[current_index, 'type'] = r[x]['type']
                activities.loc[current_index, 'distance'] = r[x]['distance']
                activities.loc[current_index, 'moving_time'] = r[x]['moving_time']
                activities.loc[current_index, 'elapsed_time'] = r[x]['elapsed_time']
                activities.loc[current_index, 'total_elevation_gain'] = r[x]['total_elevation_gain']
                activities.loc[current_index, 'end_latlng'] = r[x]['end_latlng']
                activities.loc[current_index, 'external_id'] = r[x]['external_id']

            page += 1

    activity_loc = "./activities/" + str(csvs[i])
    activities.to_csv(activity_loc)
