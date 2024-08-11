import shutil
import os

def edit_config_file(config_file_path, port, client_id, login_id, password):
    """
    Edit the specified config file to update the required parameters, including login ID and password.

    :param config_file_path: The path to the config file that needs to be edited.
    :param port: The new port number for OverrideTwsApiPort.
    :param client_id: The new client ID for OverrideTwsMasterClientID.
    :param login_id: The login ID for IbLoginId.
    :param password: The password for IbPassword.
    """
    # Define the changes to be made
    replacements = {
        'StoreSettingsOnServer': 'yes',
        'OverrideTwsApiPort': port,
        'OverrideTwsMasterClientID': client_id,
        'ReadOnlyApi': 'no',
        'AutoRestartTime': '12:00 AM',
        'AllowBlindTrading': 'yes',
        'BypassRedirectOrderWarning': 'yes',
        'IbLoginId': login_id,
        'IbPassword': password
    }

    # Read the file and store lines
    with open(config_file_path, 'r') as file:
        lines = file.readlines()

    # Check if IbLoginId and IbPassword are already in the file
    found_login_id = False
    found_password = False

    # Modify the necessary lines or append them if not found
    for i, line in enumerate(lines):
        for key in replacements:
            if line.startswith(key):
                # Replace the entire line with the new value
                lines[i] = f"{key}={replacements[key]}\n"
                if key == 'IbLoginId':
                    found_login_id = True
                if key == 'IbPassword':
                    found_password = True

    # If IbLoginId or IbPassword were not found, add them at the end
    if not found_login_id:
        lines.append(f"IbLoginId={login_id}\n")
    if not found_password:
        lines.append(f"IbPassword={password}\n")

    # Write the modified lines back to the file
    with open(config_file_path, 'w') as file:
        file.writelines(lines)

    print(f"Updated configuration in {config_file_path}")

def copy_config_file(new_name):
    """
    Copy the file 'config_viktor.ini' to the specified directory with a new name.

    :param new_name: The new name for the copied file (without the '.ini' extension).
    """
    # Define the original file path and the directory where the file is located
    original_file_path = r"C:\Users\vikto\Documents\IBC\config_viktor.ini"
    destination_directory = r"C:\Users\vikto\Documents\IBC"

    # Ensure the new name has the .ini extension
    new_file_name = f"{new_name}.ini"

    # Define the destination file path
    new_file_path = os.path.join(destination_directory, new_file_name)

    # Copy the original file to the new file path
    shutil.copyfile(original_file_path, new_file_path)

    print(f"Copied '{original_file_path}' to '{new_file_path}'")

copy_config_file("user1")
edit_config_file(r"C:\Users\vikto\Documents\IBC\user1.ini", 7498, 2, "user1", "pass1")