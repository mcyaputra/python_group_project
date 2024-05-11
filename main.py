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

print(author)
print(title)
print(content)




## Option 1: search by topic
# # TODO Replace below with actual inputs
# topic1 = "AI"
# topic2 = "crypto"
# topic3 = "technology"
# start_date = "2024-05-08" # Max 30 days prior to today's date
# end_date = "2024-05-10" # Has to be one day prior to today's date
# sort_by = "popularity"
# results_to_show = 2

# # Example if user wants to search by topic
# search_by_topic_results = news_api.search_by_topic(topic1, topic2, topic3, start_date, end_date, sort_by, results_to_show)

# # Response can be unpack into a list
# source, author, title, description, url, publishedAt, content = unpack_response(search_by_topic_results)


# ## Option 2: search by publishers
# # TODO Replace below with actual inputs
# publisher1 = "bbc.co.uk"
# publisher2 = "techcrunch.com"
# publisher3 = "engadget.com"
# start_date = "2024-05-08" # Max 30 days prior to today's date
# end_date = "2024-05-10"
# results_to_show = 2

# # Example if user wants to search by publisher
# search_by_publisher_results = news_api.search_by_publisher(publisher1, publisher2, publisher3, start_date, end_date, results_to_show)

# # Response can be unpack into a list
# source, author, title, description, url, publishedAt, content = unpack_response(search_by_publisher_results)



# ## Option 3: search by country and/or category
# # TODO Replace below with actual inputs
# # Possible options: ae ar at au be bg br ca ch cn co cu cz de eg fr gb gr hk hu id ie il in it jp kr lt lv ma mx my ng nl no nz ph pl pt ro rs ru sa se sg si sk th tr tw ua us ve za
# country = 'us'

# # Possible options: business entertainment general health science sports technology
# category = 'business'
# results_to_show = 2

# # Example if user wants to search by country and/or category, category is optional
# search_by_country_and_category_results = news_api.search_by_country(country, category, results_to_show)

# # Response can be unpack into a list
# source, author, title, description, url, publishedAt, content = unpack_response(search_by_country_and_category_results)