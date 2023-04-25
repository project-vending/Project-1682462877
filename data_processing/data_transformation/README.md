python
import os

directory = 'data_processing/data_transformation'

# Create the directory if it doesn't exist
if not os.path.exists(directory):
    os.makedirs(directory)

# Create the README.md file and write some initial documentation in it
with open(os.path.join(directory, 'README.md'), 'w') as file:
    file.write('# Data Transformation\n\n')
    file.write('This folder contains scripts for performing data transformation as part of the data pipeline.\n\n')
    file.write('## Scripts\n\n')
    file.write('- `transform.py`: Script for performing data transformation.\n')
