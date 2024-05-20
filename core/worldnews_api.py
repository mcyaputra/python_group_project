import logging
import requests

# Set up logs
logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)
formatter = logging.Formatter("%(asctime)s:%(levelname)s:%(name)s:%(funcName)s:%(message)s")

# Save logs in a log file
file_handler = logging.FileHandler("logs.log")
file_handler.setFormatter(formatter)
logger.addHandler(file_handler)

class NewsAPI:
    # Define logger as a class attribute
    logger = logger

    def __init__(self, newsapi_client) -> None:
        self.newsapi_client = newsapi_client

    def search_news(
                    self,
                    keyword1='',
                    keyword2=None,
                    keyword3=None,
                    language='en',
                    country1='',
                    country2=None,
                    country3=None,
                    min_sentiment=-1,
                    max_sentiment=1,
                    from_date=None,
                    to_date=None,
                    sort='publish-time',
                    sort_direction='DESC',
                    article_to_show=10):

        # Set up URL
        url = f"https://api.worldnewsapi.com/search-news?text={keyword1}&source-countries={country1}&language={language}&min-sentiment={min_sentiment}&max-sentiment={max_sentiment}&earliest-publish-date={from_date}&latest-publish-date={to_date}&sort={sort}&sort-direction={sort_direction}&number={article_to_show}"
        
        # Set up API key
        headers = {
            'x-api-key': self.newsapi_client
        }
        
        # Run request
        try:
            response = requests.get(url, headers=headers)
            response.raise_for_status()  # Raise an error for non-200 status codes
        except requests.exceptions.RequestException as e:
            self.logger.error(f'Error in API call: {e}')
            return None

        # Debugging information
        self.logger.info('Topic API call successful')

        result = response.json()

        return result
