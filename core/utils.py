import logging

# Set up logs
logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)
formatter = logging.Formatter("%(asctime)s:%(levelname)s:%(name)s:%(funcName)s:%(message)s")

# Save logs in a log file
file_handler = logging.FileHandler("logs.log")
file_handler.setFormatter(formatter)
logger.addHandler(file_handler)

def merge_topics(topic1, topic2, topic3) -> str:
        
        # Combine all topics
        topics = [topic1, topic2, topic3]

        # Join all topics for url search
        topics_url = " AND ".join([topic for topic in topics if topic])

        logger.info('Topics merged')
        return topics_url

def merge_publishers(publisher1, publisher2, publisher3) -> str:
        
        # Combine all domains
        publishers = [publisher1, publisher2, publisher3]

        # Join all domains for url search
        publishers_url = ", ".join([publisher for publisher in publishers if publisher])

        logger.info('Publishers merged')
        return publishers_url

def unpack_response(results) -> list:

        # Create empty lists to hold all relevant values
        source = []
        author = []
        title = []
        description = []
        url = []
        publishedAt= []
        content = []

        # Append all values into their respective list
        for res in results:
            source.append(res['source']['name'])
            author.append(res['author'])
            title.append(res['title'])
            description.append(res['description'])
            url.append(res['url'])
            publishedAt.append(res['publishedAt'])
            content.append(res['content'])

        logger.info('Responses successfully unpacked')
        return source, author, title, description, url, publishedAt, content