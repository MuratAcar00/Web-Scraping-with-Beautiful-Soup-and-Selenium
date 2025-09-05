####################
#Scraping a Web Page
####################

import requests
from bs4 import BeautifulSoup

result = requests.get("https://www.example.com")
print(result.status_code)

html = result.content

soup = BeautifulSoup(html, "html.parser")

print(soup.find("h1").text)