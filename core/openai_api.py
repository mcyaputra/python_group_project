import logging

# Set up logs
logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)
formatter = logging.Formatter("%(asctime)s:%(levelname)s:%(name)s:%(funcName)s:%(message)s")

# Save logs in a log file
file_handler = logging.FileHandler("logs.log")
file_handler.setFormatter(formatter)
logger.addHandler(file_handler)

class OpenAISummariser:
    def __init__(self, openai_client):
        self.openai_client = openai_client
     
    def execute_prompt(self, 
                       prompt, 
                       system_prompt="You are an article summariser", 
                       response_format="text"):

        seed = 123

        completion = self.openai_client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": system_prompt},
                {"role": "user", "content": prompt}
            ],
            seed=seed,
            response_format={"type": response_format}
        )
        estimation = completion.choices[0].message.content
        result = {
            "status": 200,
            "value": estimation
        }
        return result
    
    def summarise_news_content(self, 
                               content,
                               prompt_from_user=None
                               ):

        if prompt_from_user:
            prompt = prompt_from_user
        else:
            prompt = f"""
                        You are a great article summarizer. 
                        Please summarize the following text into 200-250 words consisting of:
                        1. Whats the article is about (1 paragraph)
                        2. layout the 3-5 most important takeaways in bullet points:{content}
                        3. Conclusion

                        text={content}
                        """

        result = self.execute_prompt(prompt=prompt)
		
        logger.info("Successfully summarize news content")
        return result["value"]
        
