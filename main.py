import os
from core.worldnews_api import NewsAPI
from core.utils import unpack_response
import pandas as pd

api_key = os.environ.get('WORLDNEWS_API_KEY')

'''
    To get free API KEY, go to: https://worldnewsapi.com/
'''

news_api = NewsAPI(api_key)

# TODO Replace below with actual inputs
keyword1 = "Cars" # Mandatory
keyword2 = "" # Optional
keyword3 = "" # Optional
country1 = "au" # Optional, default is au
country2 = "" # Optional
country3 = "" # Optional
min_sentiment = -1 # Optional, default is -1
max_sentiment = 1 # Optional, default is 1
from_date = '2024-05-10' # Optional, need to set default -7 days from today in GUI
to_date =  '2024-05-11' # Optional, need to set default to today in GUI
article_to_show = 5 # Optional, default is 5

# Execute search
search_result = news_api.search_news(
                        keyword1=keyword1,
                        keyword2=keyword2,
                        keyword3=keyword3,
                        country1=country1,
                        country2=country2,
                        country3=country3,
                        min_sentiment=min_sentiment,
                        max_sentiment=max_sentiment,
                        from_date=from_date,
                        to_date=to_date,
                        article_to_show=article_to_show
                    )

# Unpack search result
title, author, publish_date, content, url, sentiment, source_country = unpack_response(search_result)