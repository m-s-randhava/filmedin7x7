__author__ = 'mohanrandhava'

import csv
import json
import os.path

"""
ParseCSV converts the data in 'csv_file' and converts each record
into a json object and places all results into 'json_file'.
"""

class ParseCSV(object):

    def __init__(self, csv_file, json_file):
        self.json_file = json_file
        self.csv_file = csv_file

    def read_data(self):
        basepath = os.path.dirname(__file__)
        filepath = os.path.abspath(os.path.join(basepath, "../..", "data", self.csv_file))
        with open(filepath, 'r') as f:
            parsed_data = [row for row in csv.reader(f.read().splitlines())]
        return parsed_data

    def read_csv_as_json(self):
        basepath = os.path.dirname(__file__)
        filepath = os.path.abspath(os.path.join(basepath, "../..", "data", self.csv_file))
        f = open(filepath, 'r')
        headers = f.readline().strip().split(',')
        reader = csv.DictReader(f, headers)
        parsed_data = []
        counter = 1
        for row in reader:
            row['filmid'] = counter
            counter += 1
            parsed_data.append(row)
        return parsed_data

    def convert_csv_to_json(self):
        basepath = os.path.dirname(__file__)
        filepath = os.path.abspath(os.path.join(basepath, "../..", "data", self.json_file))
        jsonfile = open(filepath, 'w')
        for row in self.read_csv_as_json():
            json.dump(row, jsonfile)
            jsonfile.write('\n')

p = ParseCSV("film_locations_in_san_francisco.csv","film_locations_in_san_francisco.json")
p.read_csv_as_json()