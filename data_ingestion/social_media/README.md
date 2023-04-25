
import os

directory = "data_ingestion/social_media"
if not os.path.exists(directory):
    os.makedirs(directory)

with open("data_ingestion/social_media/README.md", "w") as f:
    f.write("# Social Media Data Ingestion\n\n")
    f.write("This folder contains scripts for ingesting social media data into the data pipeline.\n")
    f.write("Scripts for scraping Twitter, Facebook, and Instagram are included.\n")
    f.write("To run any of the scripts, simply execute `python <script_name>.py` in the terminal.\n")
