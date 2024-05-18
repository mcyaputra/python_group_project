import unittest
from core.openai_api import OpenAISummariser
from openai import OpenAI
import os

class TestOpenAI(unittest.TestCase):

    def setUp(self):
        self.openai_client = OpenAISummariser(openai_client=OpenAI(api_key=os.environ.get("OPENAI_API_KEY")))

    def test_prompt(self):
        prompt = "Repeat this text as it is: This prompt is working properly"

        expected_result = {'status': 200,
                           'value': "This prompt is working properly"}

        result = self.openai_client.execute_prompt(prompt=prompt)
        
        self.assertEqual(result, expected_result)

if __name__ == '__main__':
    unittest.main()