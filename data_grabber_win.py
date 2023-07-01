import os
import subprocess

# Move to appropriate directory and remove old (current) relevant files
# os.chdir("/Users/s2112263/Projects/RunClub")

# Renew access tokens and set <NAME>TOKEN variable for each user
# Charlie
subprocess.run([
    "curl",
    "-X",
    "POST",
    "https://www.strava.com/oauth/token?client_id=75401&client_secret=bb2111ddbaf0b4148ef1f9a632945e63fc6170b5&grant_type=refresh_token&refresh_token=7fd7e7bd86375240a154f8a31f6dd17cc46bd5bb",
    "-o",
    "tokens/charlieToken.json"
])
charlie_token = subprocess.run([
    "jq",
    ".access_token",
    "tokens/charlieToken.json"
], capture_output=True, text=True).stdout.strip()[1:-1]

# Matthew
subprocess.run([
    "curl",
    "-X",
    "POST",
    "https://www.strava.com/oauth/token?client_id=75401&client_secret=bb2111ddbaf0b4148ef1f9a632945e63fc6170b5&grant_type=refresh_token&refresh_token=b8fb04fb661a9ae04c9190fe28c080d3d1371d53",
    "-o",
    "tokens/matthewToken.json"
])
matthew_token = subprocess.run([
    "jq",
    ".access_token",
    "tokens/matthewToken.json"
], capture_output=True, text=True).stdout.strip()[1:-1]

# Finch
subprocess.run([
    "curl",
    "-X",
    "POST",
    "https://www.strava.com/oauth/token?client_id=75401&client_secret=bb2111ddbaf0b4148ef1f9a632945e63fc6170b5&grant_type=refresh_token&refresh_token=e9e74b9a9f80ee1955620769371aac6c3b706f85",
    "-o",
    "tokens/finchToken.json"
])
finch_token = subprocess.run([
    "jq",
    ".access_token",
    "tokens/finchToken.json"
], capture_output=True, text=True).stdout.strip()[1:-1]

# Rhys
subprocess.run([
    "curl",
    "-X",
    "POST",
    "https://www.strava.com/oauth/token?client_id=75401&client_secret=bb2111ddbaf0b4148ef1f9a632945e63fc6170b5&grant_type=refresh_token&refresh_token=90656251dfc7dddee6824f6a0b31c71faef51839",
    "-o",
    "tokens/rhysToken.json"
])
rhys_token = subprocess.run([
    "jq",
    ".access_token",
    "tokens/rhysToken.json"
], capture_output=True, text=True).stdout.strip()[1:-1]

# George
subprocess.run([
    "curl",
    "-X",
    "POST",
    "https://www.strava.com/oauth/token?client_id=75401&client_secret=bb2111ddbaf0b4148ef1f9a632945e63fc6170b5&grant_type=refresh_token&refresh_token=729a07c75e183ea989b0c5b946b0683f5a8ebe20",
    "-o",
    "tokens/georgeToken.json"
])
george_token = subprocess.run([
    "jq",
    ".access_token",
    "tokens/georgeToken.json"
], capture_output=True, text=True).stdout.strip()[1:-1]

## Jenny Token - Was used for testing, leaving here. Might use one day?
subprocess.run([
    "curl",
    "-X",
    "POST",
    "https://www.strava.com/oauth/token?client_id=75401&client_secret=bb2111ddbaf0b4148ef1f9a632945e63fc6170b5&grant_type=refresh_token&refresh_token=2aa5cdb6777ffb34d57400e9ccb61c1cb07aed45",
    "-o",
    "tokens/jennyToken.json"
])
jenny_token = subprocess.run([
    "jq",
    ".access_token",
    "tokens/jennyToken.json"
], capture_output=True, text=True).stdout.strip()[1:-1]

# Run python code to get all activities for all group and pass to <name>Activities.json file
subprocess.run(["source", "./venv/bin/activate"], shell=True)  # activate virtual environment
subprocess.run(["python", "getActivities.py"])

# [REDUNDANT] Download RunClub spreadsheet from google docs - Can remove once everyone is authorised
subprocess.run([
    "/usr/local/bin/tbx2",
    "services",
    "google",
    "sheets",
    "sheet",
    "export",
    "-id",
    "1cRPN6rl55R8WerMHN28qtz0nMM8c_L10Xa14srtAqPM",
    "-range",
    "Current Month",
    "-data",
    "./googleData.csv"
])

# countUp.py script tallies total running distances for the week and saves each to a googleData.csv file
subprocess.run(["python", "countUp.py"])
subprocess.run(["deactivate"], shell=True)  # deactivate virtual environment

# Export the new updated data to Google docs
subprocess.run(["python", "update_sheet.py"])

# Update the figures for the website
subprocess.run(["python", "analysisGraphs/distancePieChart.py"])