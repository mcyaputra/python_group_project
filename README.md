## 📝 Description
Hi, this a Python program that compiles and aggregates news articles from various sources using both web APIs and web scraping techniques. The aim is to integrate data from multiple sources, offering users richer content compared to just relying on a single news outlet. It involves building an interactive, flexible and well-structured data aggregator. The program follows object-oriented programming principles for scalability and modularity. It also includes unit testing to ensure codes are reliable and perform as expected and required. Additionally, a GUI component are added on top of the program to enhance user experience and allow for real-time exploration of news content.

## Project Organization
------------

├── main.py                <- Main entry point to the app
├── requirements.txt       <- required packages to run the app
├── README.md              <- The top-level README for developers using this project.
├── core
    ├── openai_api.py      <- Scripts to run OpenAI
    ├── utils.py           <- Utility functions to support the app
    ├── worldnews_api.py   <- Scripts to run WorldNews API
    ├── visualizations.py  <- Scripts to run visualizations
├── tests                  <- Folder containing test scripts to test all the classes and methods

------------

## ⚙️ How to run the app
1. Clone this repo into your desired folder

2. In your terminal, cd into project folder where you stored the cloned repo, run "pip install -r requirements.txt"

3. In your terminal, run "python main.py"

4. UI should pops out

5. Enter search keyword (for example: Tesla or Toyota)

6. Enter Country (for example: Australia or China)
  
7. Select date range
 
8. Click "News Search" to search articles using WorldNews API based on your selection criteria

9. Click "Web Scrape" to search articles using web scraping based on your selection criteria
  
11. Click "Visual" to view charts related to your search for additional insights

12. Click "News Summary" to get a quick summary of the articles, the summary will be performed using OpenAI

## ⚙️ How to run unit tests

1. In your terminal, cd into project folder where you stored the cloned repo

2. In your terminal, run "python -m unittest"
