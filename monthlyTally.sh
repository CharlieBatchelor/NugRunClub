#!/bin/bash
# ======================================================================================================================
# Description:
# This script moves to the RunClub area, updates tokens for each member of RunClub, then uses these to run a python
# script retrieving all member Strava uploaded activities. The activities are used in the countUp.py script to tally
# the total running distance for each user. tbx is then used to upload the updated distances to google sheets.
# ======================================================================================================================
# Move to appropriate directory and remove old(current) relevant files
cd /Users/s2112263/Projects/RunClub || exit
# ======================================================================================================================
# Renew access tokens and set <NAME>TOKEN variable for each user
# Charlie
#curl -X POST https://www.strava.com/oauth/token\?client_id\=75401\&client_secret\=bb2111ddbaf0b4148ef1f9a632945e63fc6170b5\&grant_type\=refresh_token\&refresh_token\=7fd7e7bd86375240a154f8a31f6dd17cc46bd5bb > tokens/charlieToken.json
#CHARLIETOKEN=$(/usr/local/bin/jq .access_token tokens/charlieToken.json)
#CHARLIETOKEN=$(echo $CHARLIETOKEN | sed 's/"//g')
## Matthew
#curl -X POST https://www.strava.com/oauth/token\?client_id\=75401\&client_secret\=bb2111ddbaf0b4148ef1f9a632945e63fc6170b5\&grant_type\=refresh_token\&refresh_token\=b8fb04fb661a9ae04c9190fe28c080d3d1371d53 > tokens/matthewToken.json
#MATTHEWTOKEN=$(/usr/local/bin/jq .access_token tokens/matthewToken.json)
#MATTHEWTOKEN=$(echo $MATTHEWTOKEN | sed 's/"//g')
### Finch
#curl -X POST https://www.strava.com/oauth/token\?client_id\=75401\&client_secret\=bb2111ddbaf0b4148ef1f9a632945e63fc6170b5\&grant_type\=refresh_token\&refresh_token\=e9e74b9a9f80ee1955620769371aac6c3b706f85 > tokens/finchToken.json
#FINCHTOKEN=$(/usr/local/bin/jq .access_token tokens/finchToken.json)
#FINCHTOKEN=$(echo $FINCHTOKEN | sed 's/"//g')
## Rhys
#curl -X POST https://www.strava.com/oauth/token\?client_id\=75401\&client_secret\=bb2111ddbaf0b4148ef1f9a632945e63fc6170b5\&grant_type\=refresh_token\&refresh_token\=90656251dfc7dddee6824f6a0b31c71faef51839 > tokens/rhysToken.json
#RHYSTOKEN=$(/usr/local/bin/jq .access_token tokens/rhysToken.json)
#RHYSTOKEN=$(echo $RHYSTOKEN | sed 's/"//g')
## George
#curl -X POST https://www.strava.com/oauth/token\?client_id\=75401\&client_secret\=bb2111ddbaf0b4148ef1f9a632945e63fc6170b5\&grant_type\=refresh_token\&refresh_token\=729a07c75e183ea989b0c5b946b0683f5a8ebe20 > tokens/georgeToken.json
#GEORGETOKEN=$(/usr/local/bin/jq .access_token tokens/georgeToken.json)
#GEORGETOKEN=$(echo $GEORGETOKEN | sed 's/"//g')
#
### Jenny Token - Was used for testing, leaving here. Might use one day?
#curl -X POST https://www.strava.com/oauth/token\?client_id\=75401\&client_secret\=bb2111ddbaf0b4148ef1f9a632945e63fc6170b5\&grant_type\=refresh_token\&refresh_token\=2aa5cdb6777ffb34d57400e9ccb61c1cb07aed45 > tokens/jennyToken.json
#JENNYTOKEN=`/usr/local/bin/jq .access_token tokens/jennyToken.json`
#JENNYTOKEN=$(echo $JENNYTOKEN | sed 's/"//g')

# ======================================================================================================================
# Grab profiles data and pass to json files (for testing) - Might use profile info later, leaving in.
#curl -X GET 'https://www.strava.com/api/v3/athletes/59198223?access_token='$CHARLIETOKEN -H 'accept:application/json' > charlie.json
# Matthew
#curl -X GET 'https://www.strava.com/api/v3/athletes/53574469?access_token='$MATTHEWTOKEN -H 'accept:application/json' > matthew.json
## George
#curl -X GET 'https://www.strava.com/api/v3/athletes/52789464?access_token='$GEORGETOKEN -H 'accept:application/json' > george.json
## Rhys
#curl -X GET 'https://www.strava.com/api/v3/athletes/45911804?access_token='$RHYSTOKEN -H 'accept:application/json' > rhys.json
## Finch
#curl -X GET 'https://www.strava.com/api/v3/athletes/55900866?access_token='$FINCHTOKEN -H 'accept:application/json' > finch.json
# Jenny
#curl -X GET 'https://www.strava.com/api/v3/athletes/97130785?access_token='$JENNYTOKEN -H 'accept:application/json' > jenny.json

# ======================================================================================================================
# Run python code to get all activities for all group and pass to <name>Activities.json file
source ./venv/bin/activate # activate virtual environment
#python getActivities.py

# ======================================================================================================================
# [REDUNDANT] Download RunClub spreadsheet from google docs - Can remove once everyone is authorised
/usr/local/bin/tbx services google sheets sheet export -id 1cRPN6rl55R8WerMHN28qtz0nMM8c_L10Xa14srtAqPM --range "Last Month Results" -data ./monthlyData.csv
# countUp.py script tallies total running distances for the week and saves each to a googleData.csv file
python monthlyCountUp.py
deactivate #deactivate virtual environment

# ======================================================================================================================
# Export the new updated data to Google docs:
/usr/local/bin/tbx services google sheets sheet import -id 1cRPN6rl55R8WerMHN28qtz0nMM8c_L10Xa14srtAqPM  -range "Last Month Results" -data ./monthlyData.csv

# ======================================================================================================================
# Update the figures for the website:
#python analysisGraphs/distancePieChart.py
