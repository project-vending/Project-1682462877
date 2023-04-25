
import os

# Define the file path
file_path = "data_ingestion/sensors/README.md"

# Create the file if it doesn't exist
if not os.path.exists(file_path):
    with open(file_path, "w") as f:
        # Write some text to the file
        f.write("# Data Ingestion: Sensors\n\n")
        f.write("This folder contains scripts and code for ingesting data from sensors.\n")
