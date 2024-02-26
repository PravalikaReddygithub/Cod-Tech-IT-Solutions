import requests
from bs4 import BeautifulSoup

# URL of the website to scrape
url = 'https://weather.com/en-IN/weather/today/l/b2e1f87fe0f7a92ba70229d148ad9288ee1e5b3621294eb40d7a0041353769d0'

# Send a GET request to the URL
response = requests.get(url)

# Parsing the HTML content
soup = BeautifulSoup(response.text, 'html.parser')

# Finding the location element
location_element = soup.find(class_='CurrentConditions--location--1YWj_')

# Finding the timestamp element
timestamp_element = soup.find(class_='CurrentConditions--timestamp--1ybTk')

# Finding the temperature element
temperature_element = soup.find(class_='CurrentConditions--tempValue--MHmYY')

# Finding the weather phrase element
weather_phrase_element = soup.find(class_='CurrentConditions--phraseValue--mZC_p')

# Extracting text content from elements
location = location_element.text if location_element else 'Location not available'
timestamp = timestamp_element.text if timestamp_element else 'Timestamp not available'
temperature = temperature_element.text if temperature_element else 'Temperature not available'
weather_phrase = weather_phrase_element.text if weather_phrase_element else 'Weather phrase not available'

# Print the extracted information
print(f'Location: {location}')
print(f'Timestamp: {timestamp}')
print(f'Temperature: {temperature}')
print(f'Weather Phrase: {weather_phrase}')
