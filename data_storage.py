import os
import shutil

# Define the starting directory
start_directory = "C:/Users/xiaoyawang/Documents/DC 2/full_data"
# Get the directory of the subfolders
subfolders = [f.path for f in os.scandir(start_directory) if f.is_dir()]
# print(subfolders)

# Access the folders and Move all csv files into one folder
for i in subfolders:
    source_dir = i
    target_dir = "C:/Users/xiaoyawang/Documents/DC 2/full_data"
    file_names = os.listdir(source_dir)

    for file_name in file_names:
        shutil.move(os.path.join(source_dir, file_name), target_dir)

#
street_csv_files = [f for f in os.listdir(start_directory) if f.endswith('.csv') and 'street' in f.lower()]
outcomes_files = [f for f in os.listdir(start_directory) if f.endswith('.csv') and 'outcomes' in f.lower()]
stop_files = [f for f in os.listdir(start_directory) if f.endswith('.csv') and 'stop-and-search' in f.lower()]

# Set the folder name and path
street_folder_name = 'street_data'
outcomes_folder_name = 'outcomes_data'
stop_folder_name = 'stop-and-search_data'
folder_path1 = "C:/Users/xiaoyawang/Documents/DC 2/" + street_folder_name
folder_path2 = "C:/Users/xiaoyawang/Documents/DC 2/" + outcomes_folder_name
folder_path3 = "C:/Users/xiaoyawang/Documents/DC 2/" + stop_folder_name
# Create the folder if it doesn't exist
folders = [folder_path1, folder_path2, folder_path3]
for j in folders:
    if not os.path.exists(j):
        os.makedirs(j)
# Move the files to separate folders
for file_name in street_csv_files:
    shutil.move(os.path.join(start_directory, file_name), folder_path1)

for file_name in outcomes_files:
    shutil.move(os.path.join(start_directory, file_name), folder_path2)
    
for file_name in stop_files:
    shutil.move(os.path.join(start_directory, file_name), folder_path3)