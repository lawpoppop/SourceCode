# -*- coding: Shift-JIS -*-
import requests
from bs4 import BeautifulSoup

# URL of the website you want to extract data from
url = "https://peps.python.org/pep-0263/"

# Send a GET request to the URL
response = requests.get(url)

# Check if the request was successful (status code 200)
if response.status_code == 200:
    # Parse the HTML content of the webpage
    soup = BeautifulSoup(response.content, 'html.parser')
    
    # Extract data by finding specific elements using CSS selectors or other methods
    # For example, to extract all <p> tags:
    paragraphs = soup.find_all('p')
    
    # Text to search within paragraphs
    search_text = "Unicode literals"
    
    # Iterate over each paragraph and check if the search text is present
    for paragraph in paragraphs:
        if search_text in paragraph.text:
            print("Found '{}' in paragraph:".format(search_text))
            print(paragraph.text)
            print()  # Add a newline for clarity
else:
    print("Failed to retrieve data from the URL. Status code:", response.status_code)
