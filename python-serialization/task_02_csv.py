#!/usr/bin/python3
import csv
import json

"""Convert csv to json"""


def convert_csv_to_json(csv_filename):
    """Convert csv to json"""
    with open(csv_filename, 'r', newline='') as f:
        csv_reader = csv.DictReader(f)
        data = list(csv_reader)

    json_data = json.dumps(data, indent=4)

    with open('data.json', 'w') as f_json:
        f_json.write(json_data)

    return True
