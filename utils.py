import os

def rename(bat_file_path, new_name,api):
    with open(bat_file_path, 'r') as file:
        lines = file.readlines()

    if(api == "Gateway"):
        lines[36] = f'set CONFIG=%USERPROFILE%\\Documents\\IBC\\config_{new_name}.ini\n'
    else:
        lines[32] = f'set CONFIG=%USERPROFILE%\\Documents\\IBC\\config_{new_name}.ini\n'
    with open(bat_file_path, 'w') as file:
        file.writelines(lines)

    print(f"Updated line 33 in {bat_file_path} to use config_{new_name}.ini")

def fetch_config_files(directory):
    # List to store the last names
    last_names = []

    # Iterate over all files in the directory
    for filename in os.listdir(directory):
        # Check if the file is a config file with the correct prefix and extension
        if filename.startswith("config_") and filename.endswith(".ini"):
            # Extract the last part of the name (e.g., "scott" from "config_scott.ini")
            last_name = filename[len("config_"):-len(".ini")]
            last_names.append(last_name)

    # Return the list of last names and its length
    return last_names, len(last_names)

def change_logging_path(config_file_path, name, api):
    """
    Modify the logging path in the config file on line 39.
    """
    with open(config_file_path, 'r') as file:
        lines = file.readlines()
    if(api == "Gateway"):
        lines[42] = f'set LOG_PATH=%IBC_PATH%\\Logs\\{name}\n'
    else:
        lines[38] = f'set LOG_PATH=%IBC_PATH%\\Logs\\{name}\n'
    with open(config_file_path, 'w') as file:
        file.writelines(lines)
    print(f"Updated line 39 in {config_file_path} to set LOG_PATH to %IBC_PATH%\\Logs\\{name}")

