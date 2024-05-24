import pandas as pd
import matplotlib.pyplot as plt
import os

def load_data(csv_file_path):
    """
    Loading the CSV data into a Pandas DataFrame.
    """
    try:
        return pd.read_csv(csv_file_path)
    except FileNotFoundError:
        print(f"Error: The file at path {csv_file_path} was not found.")
        raise

def plot_sentiment_vs_author(df):
    """
    Plotting sentiment vs. author.
    """
    plt.figure(figsize=(10, 6))
    plt.bar(df['author'], df['sentiment'], color='skyblue')
    plt.title('Sentiment vs. Author')
    plt.xlabel('Author')
    plt.ylabel('Sentiment')
    plt.xticks(rotation=90)
    plt.tight_layout()
    plt.show()

def plot_sentiment_vs_title(df):
    """
    Plotting sentiment vs. title using a horizontal bar chart.
    """
    plt.figure(figsize=(10, 6))
    plt.barh(df['title'], df['sentiment'], color='green')
    plt.title('title vs. Sentiment')
    plt.xlabel('Sentiment')
    plt.ylabel('Title')
    plt.tight_layout()
    plt.show()

def plot_publish_date_vs_author(df):
    """
    Plotting publish date vs. author.
    """
    plt.figure(figsize=(10, 6))
    df['publish_date'] = pd.to_datetime(df['publish_date'])
    plt.plot(df['publish_date'], df['author'],linestyle='-', marker='o', color='red')
    plt.title('Author vs Publish Date ')
    plt.xlabel('Publish Date')
    plt.ylabel('Author')
    plt.xticks(rotation=90)
    plt.tight_layout()
    plt.show()

def plot_publish_date_vs_title(df):
    """
    Plotting publish date vs. title using a line plot.
    """
    plt.figure(figsize=(10, 6))
    df['publish_date'] = pd.to_datetime(df['publish_date'])
    plt.plot(df['publish_date'], df['title'], linestyle='-', marker='o', color='purple')
    plt.title('Publish Date vs. Title')
    plt.xlabel('publish Date')
    plt.ylabel('Title')
    plt.xticks(rotation=90)
    plt.tight_layout() # Adjusting plot to ensure everything fits without overlapping
    plt.show()
    
def plot_sentiments_id(df):
    """
    Plotting Sentiments vs. Article ID using a horizontal bar plot.
    """
    df['id'] = df['id'].astype(str)
    
    plt.figure(figsize=(10, 6))
    plt.barh(df['id'], df['sentiment'], color='green')
    plt.title('Article ID vs. Sentiment')
    plt.xlabel('Sentiment')
    plt.ylabel('Article ID')
    plt.tight_layout()
    plt.show()


def generate_visualizations():
    """
    Generating and displaying visualizations based on the provided CSV file.
    
    """
    
    # Defining the CSV file path, adjusting to the project root
    csv_file_path = os.path.join('data', 'news_data_web_scrap.csv')
    
    # Debugging: Print the current working directory
    print(f"Current working directory: {os.getcwd()}")
    
    # Debug: Checking if the file exists
    if not os.path.isfile(csv_file_path):
        print(f"Error: The file at path {csv_file_path} does not exist.")
    else:
        # Loading the data
        df = load_data(csv_file_path)
        
    df = load_data(csv_file_path)
    # Generating various plots
    plot_sentiment_vs_author(df)
    plot_sentiment_vs_title(df)
    plot_publish_date_vs_author(df)
    plot_publish_date_vs_title(df)
    plot_sentiments_id(df)
