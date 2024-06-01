#!/usr/bin/python3

import csv 
import json

def convert_csv_to_json(filename):
    with open(filename, 'a+', newline='') as newfilecsv:
            csv_reader = csv.DictReader(newfilecsv)
            json_data = json.dumps(list(csv_reader), indent=4)
            
    with open('data.json', 'w') as json_file:
        json_file.write(json_data)
        
    return True
                