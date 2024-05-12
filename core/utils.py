import logging

# Set up logs
logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)
formatter = logging.Formatter("%(asctime)s:%(levelname)s:%(name)s:%(funcName)s:%(message)s")

# Save logs in a log file
file_handler = logging.FileHandler("logs.log")
file_handler.setFormatter(formatter)
logger.addHandler(file_handler)

def merge_keywords(keyword1=None, keyword2=None, keyword3=None) -> str:
        
	# Combine all keywords
	keywords = [keyword1, keyword2, keyword3]

	# Join all keywords for url search
	keywords_url = " OR ".join([keyword for keyword in keywords if keyword])

	logger.info('Keywords merged')

	# Return result if not empty
	if keywords_url == '':
		return None
	else:
		return keywords_url

def convert_countries_name_for_processing(country):
    
	# Convert country name into another format
	if country == 'Australia':
		result = 'au'
	elif country == 'Europe':
		result = 'eu'
	elif country == 'US':
		result = 'us'
	elif country == 'UK':
		result = 'gb'
	elif country == 'China':
		result = 'cn'
	elif country == 'india':
		result = 'in'
	elif country == 'Japan':
		result = 'jp'
	elif country == 'Indonesia':
		result = 'id'

	return result

def merge_countries(country1=None, country2=None, country3=None) -> str:

	# Convert country names into required formats
	if country1:
		country1 = convert_countries_name_for_processing(country1)
	if country2:
		country2 = convert_countries_name_for_processing(country2)
	if country3:
		country3 = convert_countries_name_for_processing(country3)
        
	# Combine all countries
	countries = [country1, country2, country3]

	# Join all countries for url search
	countries_url = ",".join([country for country in countries if country])

	logger.info('Countries merged')

	if countries_url == '':
		return None
	else:
		return countries_url

def unpack_response(result) -> list:

	# Create empty lists to hold all relevant values
	title = []
	author = []
	publish_date = []
	content = []
	url = []
	sentiment = []
	source_country = []

	# Append all values into their respective list
	for res in result['news']:
		title.append(res['title'])
		author.append(res['author'])
		publish_date.append(res['publish_date'])
		content.append(res['text'])
		url.append(res['url'])
		sentiment.append(res['sentiment'])
		source_country.append(res['source_country'])

	logger.info('Responses successfully unpacked')
	return title, author, publish_date, content, url, sentiment, source_country

