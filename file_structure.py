  
import os
import pathlib

# Define the folder structure
folders = ['data_ingestion', 'data_processing', 'data_storage']

# Define the subfolders for each folder
subfolders = {
    'data_ingestion': ['sensors', 'social_media', 'iot_devices'],
    'data_processing': ['data_aggregation', 'data_transformation', 'data_visualization'],
    'data_storage': ['aws', 'docker']
}

# Create the folders and subfolders
for folder in folders:
    os.makedirs(folder, exist_ok=True)
    for subfolder in subfolders[folder]:
        pathlib.Path(folder + '/' + subfolder).mkdir(parents=True, exist_ok=True)

# Create empty files in each subfolder
for folder in folders:
    for subfolder in subfolders[folder]:
        with open(folder + '/' + subfolder + '/README.md', 'w'):
            pass

