import os
import requests
import logging
from core.utils import merge_topics, merge_publishers

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

    def search_by_topic(self, 
                        topic1:str, 
                        topic2:str, 
                        topic3:str,
                        start_date, 
                        end_date, 
                        sort_by="relevancy", 
                        results_to_show=10) -> list:

        # Extract all topics
        topics_url = merge_topics(topic1, topic2, topic3)

        # Assign URL to search by topics
        url = (f'https://newsapi.org/v2/everything?q={topics_url}&from={start_date}&to={end_date}&sortBy={sort_by}&apiKey={self.newsapi_client}')
        
        # Run API call
        try:
            response = requests.get(url)
            result = response.json()
        except Exception as e:
            logger.error(f'Unsuccessful topic API call, error:{e}')

        # Convert total number of results to show into integer
        results_to_show_int = int(results_to_show)

        # Return results according to total number of results to show
        if result['status'] == 'ok':
            top_results = result['articles'][:results_to_show_int]
            logger.info('Topic API call successful')

        return top_results
    
    def search_by_publisher(self, 
                            publisher1:str, 
                            publisher2:str, 
                            publisher3:str, 
                            start_date, 
                            end_date, 
                            results_to_show=10) -> list:
        
        # Extract all domains
        publishers_url = merge_publishers(publisher1, publisher2, publisher3)

        # Assign sort by
        sort_by = 'popularity'

        # Assign URL to search by publish
        url = (f'https://newsapi.org/v2/everything?domains={publishers_url}&from={start_date}&to={end_date}&sortBy={sort_by}&apiKey={self.newsapi_client}')
        
        # Run API call
        try:
            response = requests.get(url)
            result = response.json()
        except Exception as e:
            logger.error(f'Unsuccessful publisher API call, error:{e}')

        # Convert total number of results to show into integer
        results_to_show_int = int(results_to_show)

        # Return results according to total number of results to show
        if result['status'] == 'ok':
            articles = result['articles']
            
            # Exclude removed articles
            available_articles = [article for article in articles if article['title'] != '[Removed]']
            top_results = available_articles[:results_to_show_int]
            logger.info('Publisher API call successful')
            
        return top_results

    def search_by_country(self,
                          country:str,
                          category="",
                          results_to_show=10) -> list:
        
        # Check if category exist
        if category == "": 
            url = (f"https://newsapi.org/v2/top-headlines?country={country}&apiKey={self.newsapi_client}")
        else:
            url = (f"https://newsapi.org/v2/top-headlines?country={country}&category={category}&apiKey={self.newsapi_client}")
        
        # Run API call
        try:
            response = requests.get(url)
            result = response.json()
        except Exception as e:
            logger.error(f'Unsuccessful country API call, error:{e}')

        # Convert total number of results to show into integer
        result_to_show_int = int(results_to_show)

        # Return results according to total number of results to show
        if result['status'] == 'ok':
            top_results = result['articles'][:result_to_show_int]
            logger.info('Country API call successful')
        
        return top_results


