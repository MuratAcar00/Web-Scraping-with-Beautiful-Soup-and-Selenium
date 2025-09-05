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
        <p id="paragraph">A simple HTML page for testing web scraping with beautifulSoup.</p>
        <a class = "link" href = "www.miuul.com" target = "blank" aria-label = "Miuul (Opens Miuul Page)">Click</a>
        <li>Outsider</li>
        <ul>
            <li class="list-item">Item 1</li>
            <li class="list-item">Item 2</li>
        </ul>
        <li>Outsider 2</li>
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


#HTML'de gezinme ve arama

soup = BeautifulSoup(html, "html.parser")

soup.a
soup.find("a", attrs={"class": "link", "target":"blank"})
print(soup.find("a", attrs={"class": "link", "target":"blank"}))

print(soup.find_all("li"))

print(soup.find("li", attrs={"class":"list-item"}))

