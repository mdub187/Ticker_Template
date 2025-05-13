import json
import csv

# Load JSON data
with open('data.json', 'r') as json_file:
    data = json.load(json_file)

# Open a CSV file for writing
with open('../data.csv', 'w', newline='') as csv_file:
    writer = csv.writer(csv_file)

    # Write the header (keys of the JSON object)
    if isinstance(data, list) and len(data) > 0:
        writer.writerow(data[0].keys())

        # Write the rows (values of the JSON object)
        for item in data:
            writer.writerow(item.values())
    elif isinstance(data, dict):
        writer.writerow(data.keys())
        writer.writerow(data.values())

# Convert CSV to JSON
csv_filepath('../data/data.csv')
def csv_to_json(csv_filepath, json_filepath):
    try:
        with open(csv_filepath, 'r') as csv_file:
            reader = csv.DictReader(csv_file)
            data = [row for row in reader]

        with open(json_filepath, 'w') as json_file:
            json.dump(data, json_file, indent=4)

        print(f"CSV data successfully converted to JSON and saved to {json_filepath}")
    except Exception as e:
        print(f"Error converting CSV to JSON: {e}")

# Example usage
if __name__ == "__main__":
    csv_to_json(csv_filepath, 'data.json')