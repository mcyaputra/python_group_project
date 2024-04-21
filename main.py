import os
from core.news_api import NewsAPI
from core.utils import unpack_response

api_key = os.environ.get('NEWSAPI_API_KEY')

'''
    To get free API KEY, go to: https://newsapi.org/register
'''

news_api = NewsAPI(api_key)

## Option 1: search by topic
# TODO Replace below with actual inputs
topic1 = "AI"
topic2 = "crypto"
topic3 = "technology"
start_date = "2024-04-01"
end_date = "2024-04-20"
sort_by = "popularity"
results_to_show = 2

# Example if user wants to search by topic
search_by_topic_results = news_api.search_by_topic(topic1, topic2, topic3, start_date, end_date, sort_by, results_to_show)

# Response can be unpack into a list
source, author, title, description, url, publishedAt, content = unpack_response(search_by_topic_results)



## Option 2: search by publishers
# TODO Replace below with actual inputs
publisher1 = "bbc.co.uk"
publisher2 = "techcrunch.com"
publisher3 = "engadget.com"
start_date = "2024-04-01"
end_date = "2024-04-20"
results_to_show = 2

# Example if user wants to search by publisher
search_by_publisher_results = news_api.search_by_publisher(publisher1, publisher2, publisher3, start_date, end_date, results_to_show)

# Response can be unpack into a list
source, author, title, description, url, publishedAt, content = unpack_response(search_by_publisher_results)



## Option 3: search by country and/or category
# TODO Replace below with actual inputs
# Possible options: ae ar at au be bg br ca ch cn co cu cz de eg fr gb gr hk hu id ie il in it jp kr lt lv ma mx my ng nl no nz ph pl pt ro rs ru sa se sg si sk th tr tw ua us ve za
country = 'us'

# Possible options: business entertainment general health science sports technology
category = 'business'
results_to_show = 2

# Example if user wants to search by country and/or category, category is optional
search_by_country_and_category_results = news_api.search_by_country(country, category, results_to_show)

# Response can be unpack into a list
source, author, title, description, url, publishedAt, content = unpack_response(search_by_country_and_category_results)
