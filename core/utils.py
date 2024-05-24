
def unpack_response(response):
    """
    Unpack the response dictionary into individual lists for easier handling and visualization.
    """
    title = []
    author = []
    publish_date = []
    content = []
    url = []
    sentiment = []
    source_country = []

    if response and 'news' in response:
        for news_item in response['news']:
            title.append(news_item.get('title', None))
            author.append(news_item.get('author', None))
            publish_date.append(news_item.get('publish_date', None))
            content.append(news_item.get('text', None))
            url.append(news_item.get('url', None))
            sentiment.append(news_item.get('sentiment', None))
            source_country.append(news_item.get('source_country', None))
    else:
        print("Error: Invalid or empty response.")

    return title, author, publish_date, content, url, sentiment, source_country



