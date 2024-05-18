import os
import requests
import logging
from core.utils import merge_keywords, merge_countries

# Set up logs
logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)
formatter = logging.Formatter("%(asctime)s:%(levelname)s:%(name)s:%(funcName)s:%(message)s")

# Save logs in a log file
file_handler = logging.FileHandler("logs.log")
file_handler.setFormatter(formatter)
logger.addHandler(file_handler)

class NewsAPI:
    def __init__(self, newsapi_client) -> None:
        self.newsapi_client = newsapi_client

    def search_news(
                    self,
                    keyword1,
                    keyword2=None,
                    keyword3=None,
                    language='en',
                    country1='Australia',
                    country2=None,
                    country3=None,
                    min_sentiment=-1,
                    max_sentiment=1,
                    from_date=None,
                    to_date=None,
                    sort='publish-time',
                    sort_direction='DESC',
                    article_to_show=5):

        # Combine all keywords
        keywords = merge_keywords(keyword1, keyword2, keyword3)

        # Combine all countries
        countries = merge_countries(country1, country2, country3)
        
        url = f"https://api.worldnewsapi.com/search-news?text={keywords}&language={language}&source-countries={countries}&min-sentiment={min_sentiment}&max-sentiment={max_sentiment}&earliest-publish-date={from_date}&latest-publish-date={to_date}&sort={sort}&sort-direction={sort_direction}&number={article_to_show}"

        # Set up API key
        headers = {
            'x-api-key': self.newsapi_client
        }
        
        # Run request
        try:
            response = requests.get(url, headers=headers)
        except Exception as e:
            logger.error(f'Unsuccessful topic API call, error:{e}')

        if response.status_code == 200:
            result = response.json()
            logger.info('Topic API call successful')
            return result, response.status_code
        else:
            logger.error(f"Error: {response.status_code}")

        