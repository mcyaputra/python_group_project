


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
    
    def 