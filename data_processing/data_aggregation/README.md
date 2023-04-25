
# Import the os module
import os

# Define the path to the README.md file
file_path = "data_processing/data_aggregation/README.md"

# Open the file in write mode and write to it
with open(file_path, "w") as f:
    f.write("Data Aggregation\n")
    f.write("===============\n\n")
    f.write("This folder contains scripts for performing data aggregation in our data pipeline.\n")
    f.write("The scripts are organized as follows:\n\n")
    f.write("1. `aggregate_data.py`: Script for aggregating data from various sources.\n")
    f.write("2. `merge_data.py`: Script for merging aggregated data into a single file.\n")
