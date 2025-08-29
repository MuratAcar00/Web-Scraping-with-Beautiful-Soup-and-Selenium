##########
# Getting Started
##########
# pip install beautifulsoup4

from bs4 import BeautifulSoup

html = """
<!DOCTYPE html>
    <html>
    <head>
        <title> Example HTML</title>
    </head>
    <body>
        <h1>Hello, World!</h1>
        <p>A simple HTML page for testing web scraping with beautifulSoup.</p>
        <a class = "link" href = "www.miuul.com" target = "blank" aria-label = "Miuul (Opens Miuul Page)">Click</a>
        <li>Outsider</li>
        <ul>
            <li>Item 1</li>
            <li>Item 2</li>
        </ul>
    </body>
    </html>
"""

soup = BeautifulSoup(html, "html.parser")
title = soup.title
print(title)
type(title)
title.text
title.string

#HTML dosyasını düzenleme:
print(soup.prettify())


print(soup.ul)

print(soup.li)

ul = soup.ul
print(type(ul))

print(ul.li)