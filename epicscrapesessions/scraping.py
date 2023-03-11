# from google_play_scraper import app, Sort, reviews_all

# import pandas as pd
# import numpy as np

# us_reviews = reviews_all(
#     'deezer.android.app',
#     sleep_milliseconds=0,  # defaults to 0
#     lang='en',  # defaults to 'en'
#     country='us',  # defaults to 'us'
#     sort=Sort.NEWEST,  # defaults to Sort.MOST_RELEVANT
# )

# f = open('output.txt', 'w')
# f.write(us_reviews)


import pandas as pd
import numpy as np
import json
from datetime import datetime
from app_store_scraper import AppStore


class CustomEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, datetime):
            return obj.strftime('%Y-%m-%d %H:%M:%S')
        return json.JSONEncoder.default(self, obj)


slack = AppStore(
    country='us', app_name='deezer-music-player-podcast', app_id='292738169')

slack.review()


with open('example.json', 'w') as file:
    for review in slack.reviews:
        json.dump(review, file, indent=4, cls=CustomEncoder)
        file.write(',' + '\n')
