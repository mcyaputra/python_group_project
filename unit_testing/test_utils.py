import unittest
from io import StringIO
import sys
from core.utils import unpack_response

class TestUnpackResponse(unittest.TestCase):

    def setUp(self):
        # Giving the sample response for testing
        self.sample_response = {
            "news": [
                {
                    "title": "Sample Title 1",
                    "author": "Author 1",
                    "publish_date": "2023-05-01",
                    "text": "Sample content 1",
                    "url": "http://example.com/article1",
                    "sentiment": 0.5,
                    "source_country": "US"
                },
                {
                    "title": "Sample Title 2",
                    "author": "Author 2",
                    "publish_date": "2023-05-02",
                    "text": "Sample content 2",
                    "url": "http://example.com/article2",
                    "sentiment": -0.1,
                    "source_country": "CA"
                }
            ]
        }

        self.empty_response = {"news": []}

        self.invalid_response = {}

    def test_unpack_response_with_valid_data(self):
        
        # Unpacking the response
        title, author, publish_date, content, url, sentiment, source_country = unpack_response(self.sample_response)
         
          # Asserting the unpacked data matches the expected values
        self.assertEqual(title, ["Sample Title 1", "Sample Title 2"])
        self.assertEqual(author, ["Author 1", "Author 2"])
        self.assertEqual(publish_date, ["2023-05-01", "2023-05-02"])
        self.assertEqual(content, ["Sample content 1", "Sample content 2"])
        self.assertEqual(url, ["http://example.com/article1", "http://example.com/article2"])
        self.assertEqual(sentiment, [0.5, -0.1])
        self.assertEqual(source_country, ["US", "CA"])

    def test_unpack_response_with_empty_data(self):
          # Unpacking the response
        title, author, publish_date, content, url, sentiment, source_country = unpack_response(self.empty_response)
         # Assertion of the unpacked data is empty lists
        self.assertEqual(title, [])
        self.assertEqual(author, [])
        self.assertEqual(publish_date, [])
        self.assertEqual(content, [])
        self.assertEqual(url, [])
        self.assertEqual(sentiment, [])
        self.assertEqual(source_country, [])

    def test_unpack_response_with_invalid_data(self):
          # Redirecting stdout to capture print statements
        captured_output = StringIO()
        sys.stdout = captured_output
        
         # Unpacking the response
        title, author, publish_date, content, url, sentiment, source_country = unpack_response(self.invalid_response)
        # Resetting stdout
        sys.stdout = sys.__stdout__
         # Assertion of the error message is printed and unpacked data is empty lists
        self.assertIn("Error: Invalid or empty response.", captured_output.getvalue().strip())
        
        self.assertEqual(title, [])
        self.assertEqual(author, [])
        self.assertEqual(publish_date, [])
        self.assertEqual(content, [])
        self.assertEqual(url, [])
        self.assertEqual(sentiment, [])
        self.assertEqual(source_country, [])

if __name__ == '__main__':
    unittest.main()
