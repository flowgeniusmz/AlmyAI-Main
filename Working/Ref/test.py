import csv
import json

# Replace 'data.csv' with your CSV filename
csv_file = 'data.csv'
json_file = 'data.json'

# Read the CSV and add data to a dictionary
csv_rows = []
with open(csv_file, 'r') as csvfile:
    csvreader = csv.DictReader(csvfile)
    title = csvreader.fieldnames
    for row in csvreader:
        csv_rows.extend([{title[i]:row[title[i]] for i in range(len(title))}])

# Write the data to a JSON file
with open(json_file, 'w') as jsonfile:
    jsonfile.write(json.dumps(csv_rows, indent=4))
