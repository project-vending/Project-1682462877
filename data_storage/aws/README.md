
import os

# Specify the folder path
folder_path = 'data_storage/aws'

# Create the file
with open(os.path.join(folder_path, 'README.md'), 'w') as file:
    file.write('# AWS Data Storage\n\nThis folder contains files related to AWS data storage.')
