#Runs the TWS and changes it's settings
#TODO Automatically create config files


import subprocess
import time

import utils

api = "Gateway" #or it can be "Gateway"

#Step 0: Fetch amount of config files in: "C:\Users\vikto\Documents\IBC"
users, num_of_config_files = utils.fetch_config_files(r"C:\Users\vikto\Documents\IBC")

#Step 1: Run "StartTWS.bat", change settings name and change their logging path
bat_file_path = rf"C:\IBC\Start{api}.bat"
for user in users:
    utils.rename(bat_file_path, user, api)
    utils.change_logging_path(bat_file_path, user, api)
    subprocess.run([bat_file_path], shell=True)
