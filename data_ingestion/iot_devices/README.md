
import os

# Define the path to the README.md file
path = 'data_ingestion/iot_devices/README.md'

# Create the README.md file if it doesn't exist
if not os.path.exists(path):
    with open(path, 'w') as f:
        f.write('# Data Ingestion - IoT Devices\n\nThis folder contains the data ingestion code for IoT devices.\n')
