import json
import datetime
with open('example.json', 'r') as f:
    data = json.load(f)

output = []

for review in data:
    # Convert original date string to datetime object
    original_date = datetime.datetime.fromisoformat(
        review['date'].replace('Z', '+00:00'))

    # Create new date string with desired format
    new_date_string = original_date.strftime('%Y-%m-%dT%H:%M:%SZ')
    output.append({
        'score': review['rating'],
        'title': review['title'],
        'opinion': review['review'],
        'date': new_date_string,

    })


with open('outputkevkevformat.json', 'w') as f:
    json.dump(output, f, indent=4)
    f.write(',' + '\n')
