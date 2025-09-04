import requests  # python library for HTTP requests
from bs4 import BeautifulSoup   # HTML parser

# simple function to fetch the title of a webpage
def get_page_title(url):
    """
    Fetches the page title of the given URL.
    :arg url: The URL to fetch.
    :returns: The page title of the given URL.
    """
    try:
        response = requests.get(url) # connects to the url
        response.raise_for_status()  # raises an exception for bad status codes
        # BeautifulSoup parses the .html content into a readable text
        soup = BeautifulSoup(response.text, 'html.parser')
        page_title = soup.find('title').text  # finds the title tag and converts to text
        return page_title
    # exception handling
    except requests.exceptions.RequestException as e:
        print(f"Error fetching URL: {e}")
        return None


#   example usage
url = "https://python.org/"
title = get_page_title(url)
print(title)