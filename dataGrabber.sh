#!/bin/bash
# Move to appropriate directory and remove old(current) relevant files
cd /Users/s2112263/Projects/RunClub || exit

# Remove old version of google data
#rm googleData.csv

# Renew access tokens and set to TOKEN variable for each user
# Charlie
curl -X POST https://www.strava.com/oauth/token\?client_id\=75401\&client_secret\=bb2111ddbaf0b4148ef1f9a632945e63fc6170b5\&grant_type\=refresh_token\&refresh_token\=7fd7e7bd86375240a154f8a31f6dd17cc46bd5bb > charlieToken.json
CHARLIETOKEN=$(/usr/local/bin/jq .access_token charlieToken.json)
CHARLIETOKEN=$(echo $CHARLIETOKEN | sed 's/"//g') # Remove occurancees of "

## Jenny Token
#curl -X POST https://www.strava.com/oauth/token\?client_id\=75401\&client_secret\=bb2111ddbaf0b4148ef1f9a632945e63fc6170b5\&grant_type\=refresh_token\&refresh_token\=2aa5cdb6777ffb34d57400e9ccb61c1cb07aed45 > jennyToken.json
#JENNYTOKEN=`/usr/local/bin/jq .access_token jennyToken.json`
#JENNYTOKEN=`echo $JENNYTOKEN | sed 's/"//g'` # Remove occurancees of "

# Matthew
curl -X POST https://www.strava.com/oauth/token\?client_id\=75401\&client_secret\=bb2111ddbaf0b4148ef1f9a632945e63fc6170b5\&grant_type\=refresh_token\&refresh_token\=2aa5cdb6777ffb34d57400e9ccb61c1cb07aed45 > matthewToken.json
MATTHEWTOKEN=`/usr/local/bin/jq .access_token matthewToken.json`
MATTHEWTOKEN=`echo $MATTHEWTOKEN | sed 's/"//g'` # Remove occurancees of "

# Finch
curl -X POST https://www.strava.com/oauth/token\?client_id\=75401\&client_secret\=bb2111ddbaf0b4148ef1f9a632945e63fc6170b5\&grant_type\=refresh_token\&refresh_token\=2aa5cdb6777ffb34d57400e9ccb61c1cb07aed45 > jennyToken.json
FINCHTOKEN=`/usr/local/bin/jq .access_token jennyToken.json`
FINCHTOKEN=`echo $FINCHTOKEN | sed 's/"//g'` # Remove occurancees of "

# Rhys
curl -X POST https://www.strava.com/oauth/token\?client_id\=75401\&client_secret\=bb2111ddbaf0b4148ef1f9a632945e63fc6170b5\&grant_type\=refresh_token\&refresh_token\=90656251dfc7dddee6824f6a0b31c71faef51839 > rhysToken.json
RHYSTOKEN=`/usr/local/bin/jq .access_token jennyToken.json`
RHYSTOKEN=`echo $RHYSTOKEN | sed 's/"//g'` # Remove occurancees of "

# George
curl -X POST https://www.strava.com/oauth/token\?client_id\=75401\&client_secret\=bb2111ddbaf0b4148ef1f9a632945e63fc6170b5\&grant_type\=refresh_token\&refresh_token\=729a07c75e183ea989b0c5b946b0683f5a8ebe20 > georgeToken.json
GEORGETOKEN=`/usr/local/bin/jq .access_token jennyToken.json`
GEORGETOKEN=`echo $GEORGETOKEN | sed 's/"//g'` # Remove occurancees of "

# Grab profiles data and pass to json files (for testing)
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

# Run python code to get all activities for all group and pass to <name>Activities.json file
source ./venv/bin/activate # activate virtual environment
python getCharlieActivities.py # run python code - keep venv active
python getRhysActivities.py # run python code - keep venv active
#python getMatthewActivities.py # run python code - keep venv active
python getGeorgeActivities.py # run python code - keep venv active
#python getFinchActivities.py # run python code - keep venv active
#deactivate #deactivate virtual environment

# Download RunClub spreadsheet from google docs - Can remove once everyone is authorised
/usr/local/bin/tbx services google sheets sheet export -id 1cRPN6rl55R8WerMHN28qtz0nMM8c_L10Xa14srtAqPM --range "Current Month" -data ./googleData.csv

# Edit the document with a python script?
#source ./venv/bin/activate # activate virtual environment
python countUp.py
deactivate #deactivate virtual environment

# Export the new updated data to Google docs:
/usr/local/bin/tbx services google sheets sheet import -id 1cRPN6rl55R8WerMHN28qtz0nMM8c_L10Xa14srtAqPM  -range "Current Month" -data ./googleData.csv
