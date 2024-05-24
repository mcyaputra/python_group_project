import warnings
import requests
from bs4 import BeautifulSoup
import pandas as pd
import os
import tkinter as tk

def web_scrape(news_api, keyword1, country1, from_date, to_date, result_text):
    
    """
    Use web scraping to collect news items that meet the specified criteria,
    then present the findings in a Tkinter Text widget.

    
    Setting parameters
    - news_api: A NewsAPI class instance used to retrieve news articles.
    - keyword1: The term to look for in press releases.
    - country1: The nation code for nation-specific news article filtering.
    - from_date: The news search's start date.
    - to_date: The news search's expiration date.
    - result_text: A Text widget for Tkinter that shows the outcomes.
    """
    
    # Search for news articles using the NewsAPI
    search_result = news_api.search_news(
        keyword1=keyword1,
        country1=country1,
        from_date=from_date,
        to_date=to_date,
        article_to_show=10
    )
    
    # Creating an empty list to store DataFrame objects
    dfs = []
    
    # Checking if 'news' field exists in search_result
    if 'news' in search_result:
        articles = search_result['news']
        
        # Looping through each article in the search results
        for article in articles:
            url = article['url']
            response = requests.get(url)
            soup = BeautifulSoup(response.text, 'html.parser')
            
            # Extracting article id
            article_id = article['id']
            
            # Extracting article title
            title = soup.find('h1').text.strip() if soup.find('h1') else "Title Not Found"
            
            # Extracting and cleaning article summary
            summary = article.get('summary', 'Summary Not Found')
            summary_text = clean_summary(summary)

            # Extracting article publication date
            publish_date = article['publish_date']
            
            # Extracting article language
            language = article['language']
            
            # Extracting article source country
            source_country = article['source_country']
            
            # Extracting article sentiment
            sentiment = article['sentiment']
            
            # Extracting article image URL
            image = article['image']
            
            # Extracting author
            author = article.get('author', 'Author Not Found')  # Use .get() method with default value
            
            # Creating a DataFrame for the current article
            df = pd.DataFrame({'id': [article_id], 'title': [title], 'summary': [summary_text],
                               'url': [url], 'image': [image], 'publish_date': [publish_date],
                               'language': [language], 'source_country': [source_country],
                               'sentiment': [sentiment],
                               'author': [author]})
            
            # Append the DataFrame to the list
            dfs.append(df)
    else:
        print("No 'news' field found in search_result.")
    
    # Concatenating all DataFrames in the list
    if dfs:
        df = pd.concat(dfs, ignore_index=True)
        
        # Getting the current working directory
        current_directory = os.getcwd()

        # Defining the directory where you want to save the CSV file
        save_directory = os.path.join(current_directory, 'data')

        # Creating the directory if it doesn't exist
        os.makedirs(save_directory, exist_ok=True)

        # Defining the file path
        csv_file_path = os.path.join(save_directory, 'news_data_web_scrap.csv')
        
        # Saving the DataFrame to a CSV file
        df.to_csv(csv_file_path, index=False)
        
        # Displaying the DataFrame on the GUI interface
        display_dataframe(df, result_text)
    else:
        print("No articles found.")

def clean_summary(summary):
    # Checking if the summary resembles a filename
    if summary.endswith('.html') or summary.endswith('.htm'):
        # If it resembles a filename, this will try to read and parse it as HTML
        try:
            with open(summary, 'r') as file:
                html_content = file.read()
                soup = BeautifulSoup(html_content, 'html.parser')
                return soup.get_text()
        except FileNotFoundError:
            return "Summary File Not Found"
    else:
        # If it doesn't resemble a filename,it would assume it's HTML markup and parse it
        with warnings.catch_warnings():
            warnings.simplefilter("ignore", category=UserWarning)  # Suppressing MarkupResemblesLocatorWarning
            soup = BeautifulSoup(summary, 'html.parser')
        return soup.get_text()

def display_dataframe(df, result_text):
    # Clearing the result_text Text widget
    result_text.delete("1.0", tk.END)
    
    # Displaying the DataFrame in the result_text Text widget
    for index, row in df.iterrows():
        result_text.insert(tk.END, "id: {}\n".format(row['id']))
        result_text.insert(tk.END, "title: {}\n".format(row['title']))
        result_text.insert(tk.END, "summary: {}\n".format(row['summary']))
        result_text.insert(tk.END, "url: {}\n".format(row['url']))
        result_text.insert(tk.END, "image: {}\n".format(row['image']))
        result_text.insert(tk.END, "publish_date: {}\n".format(row['publish_date']))
        result_text.insert(tk.END, "language: {}\n".format(row['language']))
        result_text.insert(tk.END, "source_country: {}\n".format(row['source_country']))
        result_text.insert(tk.END, "sentiment: {}\n".format(row['sentiment']))
        result_text.insert(tk.END, "author: {}\n".format(row['author']))
        result_text.insert(tk.END, "\n")
