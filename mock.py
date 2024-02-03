import os
import shutil 
import subprocess

def copy_to_multiple_destinations(source_folder, destination_folders):
    try:
        for destination_folder in destination_folders:
            for item in os.listdir(source_folder):
                source_item = os.path.join(source_folder, item)
                destination_item = os.path.join(destination_folder, item)

                if os.path.isdir(source_item):
                    # If the item is a directory, use shutil.copytree to copy it recursively
                    shutil.copytree(source_item, destination_item, dirs_exist_ok=True)
                else:
                    # If the item is a file, use shutil.copy2 to copy it
                    shutil.copy2(source_item, destination_item)
            
    except Exception as e:
        print(f"An error occurred: {e}")

def get_all_folders(folder_path):
    try:
        # Get a list of all items in the folder
        all_items = os.listdir(folder_path)

        # Filter out only the folders
        folders = [item for item in all_items if os.path.isdir(os.path.join(folder_path, item)) and not item == 'solution']

        return folders
    except Exception as e:
        print(f"An error occurred: {e}")
        return []

folder_path = './'

destination_folders = get_all_folders(folder_path)
for i in range(len(destination_folders)):
    destination_folders[i] = folder_path + destination_folders[i]

copy_to_multiple_destinations('./solution', destination_folders)


def run_python_file_in_folders(file_name, destination_folders):
    try:
        for destination_folder in destination_folders:
            script_path = os.path.join(destination_folder, file_name)
            
            if os.path.isfile(script_path) and script_path.endswith(".py"):
                # Run the Python script
                current_directory = os.getcwd()
                os.chdir(destination_folder)
                
                print('Running results for: ', destination_folder)
                # Run the command and wait for it to finish
                output = subprocess.check_output(f"python3 {file_name}", shell=True, text=True)
                print(output)
                
                print('----------------------')
                print('\n')
                
                # Change back to the original working directory
                os.chdir(current_directory)
            else:
                print(f"Script '{file_name}' not found in '{destination_folder}'.")
    except Exception as e:
        print(f"An error occurred: {e}")

run_python_file_in_folders('test.py', destination_folders)