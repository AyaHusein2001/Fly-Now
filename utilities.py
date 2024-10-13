import csv
import os

def _get_latest_id( file_path,field):
    
    """utility function to get the latest ID from a file, to determine what will be the next id of the entity ."""
    if not os.path.isfile(file_path):
        return 0
    
    with open(file_path, mode='r', newline='') as file:
        reader = csv.DictReader(file)
        last_id = 0
        for row in reader:
            last_id = int(row[field])
        return last_id 