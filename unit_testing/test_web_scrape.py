import unittest
import warnings
from unittest.mock import patch, call
import pandas as pd
import requests
from io import StringIO
from bs4 import BeautifulSoup
import tkinter as tk
import sys, os
# Adding the directory containing 'core' to the Python path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from core.web_scrape import web_scrape, clean_summary, display_dataframe

class TestWebScrape(unittest.TestCase):

    def setUp(self):
        
        # Setting up a sample DataFrame for testing
        self.sample_data = StringIO(
            """id,title,summary,url,image,publish_date,language,source_country,sentiment,author
            1,Title1,Summary1,http://example.com/article1,http://example.com/image1.jpg,2023-05-01,en,US,0.5,Author1"""
        )
        self.df = pd.read_csv(self.sample_data)

        # Mocking result_text widget
        self.result_text = tk.Text()

    @patch('requests.get')
    def test_web_scrape(self, mock_get):
        
        """
        Test the web_scrape function that ensures it correctly scrapes and processes the articles.
        """
        # Mocking the HTTP response for requests.get
        mock_response = requests.Response()
        mock_response.status_code = 200
        mock_response._content = b'<html><h1>Title1</h1><p>Summary1</p></html>'
        mock_get.return_value = mock_response
        
        # Mocking the NewsAPI class and its search_news method
        class MockNewsAPI:
            def search_news(self, keyword1, country1, from_date, to_date, article_to_show):
                return {
                    'news': [
                        {
                            'id': 1,
                            'url': 'http://example.com/article1',
                            'publish_date': '2023-05-01',
                            'language': 'en',
                            'source_country': 'US',
                            'sentiment': 0.5,
                            'image': 'http://example.com/image1.jpg',
                            'author': 'Author1',
                            'summary': 'Summary1'
                        }
                    ]
                }

        news_api = MockNewsAPI()
        # Calling web_scrape function with mock data
        web_scrape(news_api, 'test', 'US', '2023-05-01', '2023-05-02', self.result_text)
        
        # Expected result text to be shown in the GUI interface
        expected_text = (
            "id: 1\n"
            "title: Title1\n"
            "summary: Summary1\n"
            "url: http://example.com/article1\n"
            "image: http://example.com/image1.jpg\n"
            "publish_date: 2023-05-01\n"
            "language: en\n"
            "source_country: US\n"
            "sentiment: 0.5\n"
            "author: Author1\n"
        )
        
        # Asserting that the displayed text matches the expected text
        self.assertEqual(self.result_text.get("1.0", tk.END).strip(), expected_text.strip())

    @patch('builtins.open', new_callable=unittest.mock.mock_open, read_data="<html><body>Summary Content</body></html>")
    def test_clean_summary_with_filename(self, mock_open):
        
        """
        Testing the clean_summary function with a filename that ensures it correctly reads and cleans the summary.
        """
        summary = 'fakefile.html'
        cleaned_summary = clean_summary(summary)
        self.assertEqual(cleaned_summary, 'Summary Content')

    def test_clean_summary_with_html_content(self):
        
        """
        Testing the clean_summary function with HTML content that ensures it correctly parses and cleans the summary.
        """
        summary = '<html><body>Summary Content</body></html>'
        cleaned_summary = clean_summary(summary)
        self.assertEqual(cleaned_summary, 'Summary Content')

    def test_clean_summary_with_non_html_content(self):
        
        """
        Testing the clean_summary function with plain text content that ensures it returns the plain text unchanged.
        """
        summary = 'Plain text summary'
        cleaned_summary = clean_summary(summary)
        self.assertEqual(cleaned_summary, 'Plain text summary')

    @patch('tkinter.Text')
    def test_display_dataframe(self, mock_text):
        
        """
        Testing the display_dataframe function that ensures it correctly inserts DataFrame data into a Text widget.
        """
        result_text = mock_text()
        display_dataframe(self.df, result_text)

        expected_text = (
            "id: 1\n"
            "title: Title1\n"
            "summary: Summary1\n"
            "url: http://example.com/article1\n"
            "image: http://example.com/image1.jpg\n"
            "publish_date: 2023-05-01\n"
            "language: en\n"
            "source_country: US\n"
            "sentiment: 0.5\n"
            "author: Author1\n"
        )

        # Checking all calls to insert
        calls = [
            call(tk.END, "id: 1\n"),
            call(tk.END, "title: Title1\n"),
            call(tk.END, "summary: Summary1\n"),
            call(tk.END, "url: http://example.com/article1\n"),
            call(tk.END, "image: http://example.com/image1.jpg\n"),
            call(tk.END, "publish_date: 2023-05-01\n"),
            call(tk.END, "language: en\n"),
            call(tk.END, "source_country: US\n"),
            call(tk.END, "sentiment: 0.5\n"),
            call(tk.END, "author: Author1\n"),
            call(tk.END, "\n")
        ]

        result_text.insert.assert_has_calls(calls, any_order=False)

if __name__ == '__main__':
    # This Suppresses specific warnings if necessary
    warnings.filterwarnings("ignore", category=DeprecationWarning)
    unittest.main()
