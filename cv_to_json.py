import datetime
import json
file = open("data/reviews_spotify.csv", 'r')
f_out = open('newfile.txt', 'w')


for line in file:
    date_str, opinion, score, thumbs_up, replies = line.strip().split(",", 4)

    score = score.strip('"')
    opinion = opinion.strip('"')

    # Escape any remaining double quotes within the opinion field
    opinion = opinion.replace('"', '\\"')

    # Remove any newlines within the opinion field
    opinion = opinion.replace('\n', '')

    # Convert the date string to a datetime object (source: internet)
    dt = datetime.datetime.strptime(date_str, "%Y-%m-%d %H:%M:%S")

    # Format the datetime object as an ISO 8601 timestamp
    iso_date = dt.isoformat(timespec='seconds') + 'Z'

    output_dict = {
        "score": score,
        "title": "",
        "opinion": opinion,
        "date": iso_date,
        "thumbs_up": thumbs_up
    }

    # Print the output dictionary
    # print(output_dict)

    output_str = json.dumps(output_dict, ensure_ascii=False, indent=4)
    f_out.write(output_str)
    f_out.write('\n')
