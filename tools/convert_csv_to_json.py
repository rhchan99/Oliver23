import csv
import json
import sys


def convert_csv_to_json(csv_file, json_file):
    # Read the CSV file
    data = []
    with open(csv_file, 'r') as file:
        csv_data = csv.DictReader(file)

        # Convert CSV data to a list of dictionaries
        for row in csv_data:
            data.append(row)

    # Write the data to a JSON file
    with open(json_file, 'w') as file:
        json.dump(data, file, indent=4)


# Usage example
#convert_csv_to_json('input.csv', 'output.json')
if __name__ == "__main__":
    csv_file = sys.argv[1]
    json_file = sys.argv[2]
    convert_csv_to_json(csv_file, json_file)
