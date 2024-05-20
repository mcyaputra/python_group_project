import unittest
from unittest.mock import Mock
from core.worldnews_api import NewsAPI

class TestNewsAPI(unittest.TestCase):

    def setUp(self):
        
        # Mocking the news API client
        self.mock_newsapi_client = "mock_api_key"
        self.newsapi = NewsAPI(newsapi_client=self.mock_newsapi_client)
        
    def test_search_news(self):
        
        # Mocking response from the API
        mock_response = {
            "status": "ok",
            "articles": [
                {"title": "Article 1", "description": "Description 1"},
                {"title": "Article 2", "description": "Description 2"}
            ]
        }

        # Mocking the requests.get method
        
        with unittest.mock.patch('core.worldnews_api.requests.get') as mock_get:
            
             # Setting up the return value of the mocked get method
            mock_get.return_value.json.return_value = mock_response

             # Calling the method to be tested
            result = self.newsapi.search_news(keyword1='keyword1', country1='country1')

             # Asserting that the mock method was called with the expected arguments
            mock_get.assert_called_once_with(
                f"https://api.worldnewsapi.com/search-news?text=keyword1&source-countries=country1&language=en&min-sentiment=-1&max-sentiment=1&earliest-publish-date=None&latest-publish-date=None&sort=publish-time&sort-direction=DESC&number=10",
                headers={'x-api-key': 'mock_api_key'}
            )

         # Asserting the result
        self.assertEqual(result, mock_response)

if __name__ == '__main__':
    unittest.main()
