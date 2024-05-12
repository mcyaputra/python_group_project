import os
from core.worldnews_api import NewsAPI
from openai import OpenAI
from core.utils import unpack_response
from core.openai_api import OpenAISummariser

'''
    To get a free World News API KEY, go to: https://worldnewsapi.com/
'''
news_api_key = os.environ.get('WORLDNEWS_API_KEY')

'''
    To get a free OpenAI API KEY, go to: https://openai.com/index/openai-api/ 
'''
OPENAI_CLIENT = OpenAI(
	api_key=os.environ.get("OPENAI_API_KEY")
)
open_AI = OpenAISummariser(openai_client=OPENAI_CLIENT)

news_api = NewsAPI(news_api_key)

# TODO Replace below with actual inputs
keyword1 = "Cars" # Mandatory
keyword2 = "" # Optional
keyword3 = "" # Optional

# List of available countries: Australia, Europe, US, UK, China, India, Japan, Indonesia
country1 = "Australia" # Optional, default is Australia
country2 = "" # Optional
country3 = "" # Optional
min_sentiment = -1 # Optional, default is -1
max_sentiment = 1 # Optional, default is 1
from_date = '2024-05-11' # Optional, need to set default -1 day from today in GUI
to_date =  '2024-05-12' # Optional, need to set default to today in GUI
article_to_show = 5 # Optional, default is 5

# Execute search
search_result = news_api.search_news(
                        keyword1=keyword1,
                        keyword2=keyword2,
                        keyword3=keyword3,
                        country1=country1,
                        country2=country2,
                        country3=country3,
                        min_sentiment=min_sentiment,
                        max_sentiment=max_sentiment,
                        from_date=from_date,
                        to_date=to_date,
                        article_to_show=article_to_show
                    )

# Unpack search result
title, author, publish_date, content, url, sentiment, source_country = unpack_response(search_result)

# Method to summarize news content in 250 words, highlighting 3-5 most important takeaways in bullet points
# We can let users choose whether they want to get a quick summary or not based on title etc
summary_result = open_AI.summarise_news_content(content=content[0]) ## TODO replace content with actual news content