import unittest
from unittest.mock import MagicMock, patch
from core.openai_api import OpenAISummariser

class TestOpenAISummariser(unittest.TestCase):

    def setUp(self):
        
        # Mocking the OpenAI client and its execute_prompt method
        self.mock_openai_client = MagicMock()
        self.summariser = OpenAISummariser(openai_client=self.mock_openai_client)
        
        # Mocking completion response
        self.mock_completion_response = {
            "status": 200,
            "value": "This is a summary."
        }

    @patch('core.openai_api.OpenAISummariser.execute_prompt')
    def test_execute_prompt(self, mock_execute_prompt):
        mock_execute_prompt.return_value = self.mock_completion_response
             # Testing the execute_prompt method
        response = self.summariser.execute_prompt("Summarise this article.")
          # Assertion to ensure that execute_prompt is called once and response values are correct
        mock_execute_prompt.assert_called_once()
        self.assertEqual(response["status"], 200)
        self.assertEqual(response["value"], "This is a summary.")

    @patch('core.openai_api.OpenAISummariser.execute_prompt')
    def test_summarise_news_content_with_default_prompt(self, mock_execute_prompt):
        mock_execute_prompt.return_value = {"status": 200, "value": "This is a summary."}
          
          # Testing summarise_news_content method with default prompt
        content = "This is the content of the news article."
        summary = self.summariser.summarise_news_content(content)
               # Asserting that summary matches the expected value
        self.assertEqual(summary, "This is a summary.")

    @patch('core.openai_api.OpenAISummariser.execute_prompt')
    def test_summarise_news_content_with_user_prompt(self, mock_execute_prompt):
        mock_execute_prompt.return_value = {"status": 200, "value": "This is a summary."}
          
          # Testing summarise_news_content method with user prompt
        content = "This is the content of the news article."
        user_prompt = "Please summarise the following news article."
        summary = self.summariser.summarise_news_content(content, prompt_from_user=user_prompt)
        
         #Asserting that summary matches the expected value
        self.assertEqual(summary, "This is a summary.")

if __name__ == '__main__':
    unittest.main()
