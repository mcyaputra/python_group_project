from collections import Counter
import nltk
from nltk.corpus import stopwords
from matplotlib import pyplot as plt
from wordcloud import WordCloud
import string
import logging

# Set up logs
logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)
formatter = logging.Formatter("%(asctime)s:%(levelname)s:%(name)s:%(funcName)s:%(message)s")

# Save logs in a log file
file_handler = logging.FileHandler("logs.log")
file_handler.setFormatter(formatter)
logger.addHandler(file_handler)

class VisualizeWords:

    def __init__(self, text=None):
        self.text = text
    
    def tokenize_words(self, text) -> list:
        
        # Tokenize text
        try:
            tokens = nltk.word_tokenize(text.lower())

            logger.info("Successfully tokenize text")
            return tokens
        
        except Exception as e:
            logger.error(f"Error: {e}")

    def remove_stop_words(self, tokens) -> list:

        # Set up list of words and punctuations to remove
        stop_words = set(stopwords.words("English"))
        punctuations = set(string.punctuation)
        additional_stop_words = ("'s", "``", "`", "''", "'", "'d", "'ve", "said", "lot", "get", "take", "like", "'re", "n't", "'ll")

        # Remove unwanted words and punctuations
        try:
            tokens_filtered = [word for word in tokens if word not in stop_words and word not in punctuations and word not in additional_stop_words]

            logger.info("Successfully remove stop words")
            return tokens_filtered
        
        except Exception as e:
            logger.error(f"Error: {e}")

    def visualize_words(self, text=None):
        
        # Tokenize words
        tokens = self.tokenize_words(text=self.text)

        # Remove stop words
        tokens_filtered = self.remove_stop_words(tokens=tokens)

        # Join words into a string
        word_string = " ".join(tokens_filtered)

        # Set up word cloud
        word_cloud = WordCloud(background_color="white").generate(word_string)

        logger.info("Successfully visualize words")

        # Show word cloud
        plt.figure(figsize = (10, 10))
        plt.imshow(word_cloud)
        plt.axis("off")