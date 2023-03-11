# First used an online converter for cv to json, then json to json for right formatting
import json
from datetime import datetime
# Open the existing JSON file
with open('./csvjson.json', 'r') as f:
    json_data = f.read()

# Load the JSON data
data = json.loads(json_data)

# Create a new list with reordered fields
new_data = []
for item in data:
    new_item = {
        'score': item['rating'],
        'title': '',
        'opinion': item['review'],
        'date': (datetime.strptime(item['Year'], '%Y-%m-%d %H:%M:%S')).strftime('%Y-%m-%dT%H:%M:%SZ')
    }
    new_data.append(new_item)

# Convert the new data to JSON format
json_result = json.dumps(new_data, indent=2)

# Write the updated JSON to a file
with open('./out.json', 'w') as f:
    f.write(json_result)


