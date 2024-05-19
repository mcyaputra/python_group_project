import tkinter as tk
from tkinter import ttk
from core.worldnews_api import NewsAPI
from core.web_scrape import web_scrape
from core.utils import unpack_response
from core.visualization import generate_visualizations
from core.country_code import country_code
from core.openai_api import OpenAISummariser
import threading
import os
import pandas as pd
from tkcalendar import DateEntry
from openai import OpenAI
import queue

# Initialisation of main Tkinter window
root = tk.Tk()
root.title("News Search")
root.tk.call('wm', 'iconphoto', root._w, tk.PhotoImage(file='./images/analytics.png')) # Set your icon file path
title_font = ('cursive', 12, 'bold')
root.option_add('*Font', title_font)
root.option_add('*foreground', 'black')

'''
    To get a free World News API KEY, go to: https://worldnewsapi.com/
'''
# Initializing WorldnewsAPI
news_api_key = "Enter Your API Key"
news_api = NewsAPI(news_api_key)

# Queueing for thread communication
queue = queue.Queue()

# country_code() function call to get country code dictionary
country_codes = country_code()

# Variable to store the selected country code
selected_country_code = None  

# Event handler function for selecting the country
def on_country_select(event):
    global selected_country_code
    selected_country = country_combobox.get()
    if selected_country in country_codes:
        selected_country_code = country_codes[selected_country]
        print(f"Selected Country: {selected_country} | Country Code: {selected_country_code}")
    else:
        print(f"Country code not found for {selected_country}")


# search news function to search news based on inputs
def search_news():
    keyword1 = keyword_entry.get()
    country1 = selected_country_code  # Use the selected country code
    from_date = from_date_entry.get_date()
    to_date = to_date_entry.get_date()
    
    def search_news_thread():
        try:
            set_status("Searching...")
            search_result = news_api.search_news(
                keyword1=keyword1,
                country1=country1,
                from_date=from_date,
                to_date=to_date,
                article_to_show=5
            )
            
            title, author, publish_date, content, url, sentiment, source_country = unpack_response(search_result)
            
            if not title:  # Check if no data was returned
                raise ValueError("No data returned from the search.")
            
            save_to_csv(title, author, publish_date, content, url, sentiment, source_country)
            
            result_text_data = ""
            for i in range(len(title)):
                result_text_data += f"Title: {title[i]}\n"
                result_text_data += f"Author: {author[i]}\n"
                result_text_data += f"Publish Date: {publish_date[i]}\n"
                result_text_data += f"Content: {content[i]}\n"
                result_text_data += f"URL: {url[i]}\n"
                result_text_data += f"Sentiment: {sentiment[i]}\n"
                result_text_data += f"Source Country: {source_country[i]}\n\n"
            
            queue.put(("search_result", result_text_data))
            queue.put(("status", "Search completed."))
        except Exception as e:
            queue.put(("status", f"Error: {str(e)}"))
    result_text.delete("1.0", tk.END)
    search_thread = threading.Thread(target=search_news_thread)
    search_thread.start()

# Function for initiating web scraping
def on_web_scrape():
    keyword1 = keyword_entry.get()
    country1 = selected_country_code  # Use the selected country code
    from_date = from_date_entry.get_date()
    to_date = to_date_entry.get_date()
    
    def web_scrape_thread():
        try:
            set_status("Scraping...")
            web_scrape(news_api, keyword1, country1, from_date, to_date, result_text)
            queue.put(("status", "Web scraping completed."))
        except Exception as e:
            queue.put(("status", f"Error: {str(e)}"))
            
    result_text.delete("1.0", tk.END)
    scrape_thread = threading.Thread(target=web_scrape_thread)
    scrape_thread.start()

#Function for saving search results to CSV
def save_to_csv(title, author, publish_date, content, url, sentiment, source_country):
    df = pd.DataFrame({
        'Title': title,
        'Author': author,
        'Publish Date': publish_date,
        'Content': content,
        'URL': url,
        'Sentiment': sentiment,
        'Source Country': source_country
    })
    
    current_directory = os.getcwd()
    save_directory = os.path.join(current_directory, 'data')
    os.makedirs(save_directory, exist_ok=True)
    csv_file_path = os.path.join(save_directory, 'news_data_search.csv')
    
    df.to_csv(csv_file_path, index=False)

# Function that generates and displays visualizations
def show_visuals():
    try:
        generate_visualizations()  # Call the function to generate and display visualizations
        queue.put(("status", "Visualizations generated."))
    except Exception as e:
        queue.put(("status", f"Error: {str(e)}"))

# Event handler to select the from date
def on_from_date_selected(event):
    global from_date
    from_date = from_date_entry.get_date()

# Event handler to select the to date
def on_to_date_selected(event):
    global to_date
    to_date = to_date_entry.get_date()

# Function that sets status message
def set_status(message):
    queue.put(("status", message))

'''
    To get a free OpenAI API KEY, go to: https://openai.com/index/openai-api/ 
'''
#Initializing OpenAI client
OPENAI_CLIENT = OpenAI(
    api_key="Enter your API Key"
    # api_key=os.environ.get("OPENAI_API_KEY")
)
open_ai = OpenAISummariser(openai_client=OPENAI_CLIENT)

# Function that summarizes news content
def summarize_news():
    def summarize_news_thread():
        try:
            # Reading the CSV file to get all the content
            df = pd.read_csv('data/news_data_search.csv')
            all_content = df['Content'].str.cat(sep='\n\n')
            
            # Passing all the content together to the summarization function
            summary = open_ai.summarise_news_content(all_content)
            
            queue.put(("summary", summary))
            queue.put(("status", "News summary generated."))
        except Exception as e:
            queue.put(("summary_error", str(e)))
            queue.put(("status", f"Error: {str(e)}"))
    
    result_text.delete("1.0", tk.END)  # Clear the result text before starting the summary
    summarize_thread = threading.Thread(target=summarize_news_thread)
    summarize_thread.start()

# Function processes the queue for threading communication
def process_queue():
    while not queue.empty():
        try:
            task, data = queue.get(0)
            if task == "search_result" or task == "summary":
                result_text.delete("1.0", tk.END)
                result_text.insert(tk.END, data)
            elif task == "status":
                status_label.config(text=data)
            elif task == "summary_error":
                result_text.delete("1.0", tk.END)
        except queue.Empty:
            pass
    root.after(100, process_queue)

# UI elements creation and placement
keyword_label = ttk.Label(root, text="Keyword:")
keyword_entry = ttk.Entry(root, width=25)
keyword_label.grid(row=0, column=0, padx=5, pady=5, sticky="e")
keyword_entry.grid(row=0, column=1, padx=5, pady=5)

country_label = ttk.Label(root, text="Country:")
country_combobox = ttk.Combobox(root, values=list(country_codes.keys()), width=23)  # Adjust for combobox
country_label.grid(row=1, column=0, padx=5, pady=5, sticky="e")
country_combobox.grid(row=1, column=1, padx=5, pady=5)
country_combobox.bind("<<ComboboxSelected>>", on_country_select)

# Creating the To Date DateEntry
from_date_label = ttk.Label(root, text="From Date:")
from_date_entry = DateEntry(root, width=23)  # Adjust for DateEntry
from_date_label.grid(row=2, column=0, padx=5, pady=5, sticky="e")
from_date_entry.grid(row=2, column=1, padx=5, pady=5)
from_date_entry.bind("<<DateEntrySelected>>", on_from_date_selected)

# Creating the To Date DateEntry
to_date_label = ttk.Label(root, text="To Date:")
to_date_entry = DateEntry(root, width=23)  # Adjust for DateEntry
to_date_label.grid(row=3, column=0, padx=5, pady=5, sticky="e")
to_date_entry.grid(row=3, column=1, padx=5, pady=5)
to_date_entry.bind("<<DateEntrySelected>>", on_to_date_selected)

# Buttons

search_button = tk.Button(root, text="News Search", command=search_news, bg='dark blue', fg='white')
search_button.grid(row=4, column=0, padx=(5, 2), pady=5, sticky="ew")

web_scrape_button = tk.Button(root, text="Web Scrape", command=on_web_scrape, bg='dark blue', fg='white')
web_scrape_button.grid(row=4, column=1, padx=2, pady=5, sticky="ew")


visuals_button = tk.Button(root, text="Visuals", command=show_visuals, bg='dark blue', fg='white')
visuals_button.grid(row=4, column=2, padx=2, pady=5, sticky="ew")

news_summary_button = tk.Button(root, text="News Summary", command=summarize_news, bg='dark blue', fg='white')
news_summary_button.grid(row=4, column=3, padx=2, pady=5, sticky="ew")

result_text = tk.Text(root, height=20, width=100)
result_text.grid(row=5, column=0, columnspan=4, padx=10, pady=10)

scrollbar = ttk.Scrollbar(root, orient='vertical', command=result_text.yview)
scrollbar.grid(row=5, column=4, sticky='ns')
result_text.config(yscrollcommand=scrollbar.set)

status_label = ttk.Label(root, text="", relief="sunken", anchor="w")
status_label.grid(row=6, column=0, columnspan=5, sticky="ew", padx=5, pady=5)

# Starting the queue processing
root.after(100, process_queue)

# Starting the Tkinter main loop
root.mainloop()
