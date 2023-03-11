import pandas as pd
import numpy as np
import json
from datetime import datetime
from app_store_scraper import AppStore

# Use this encoder to parse the date correctly / put it in correct format for mach. learning
class CustomEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, datetime):
            return obj.strftime('%Y-%m-%d %H:%M:%S')
        return json.JSONEncoder.default(self, obj)


# Some prebuilt python package that scrapes the appstore
slack = AppStore(
    country='us', app_name='deezer-music-player-podcast', app_id='292738169')

# Get reviews, blocking call, stops automagically after a while
slack.review()


# Create file for output
with open('output.json', 'w') as file:
    for review in slack.reviews:
        json.dump(review, file, indent=4, cls=CustomEncoder)
        file.write(',' + '\n')
