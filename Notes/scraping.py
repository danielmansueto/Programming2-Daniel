# web scraping with beautiful soup

from bs4 import BeautifulSoup
import requests

url = "http://quotes.toscrape.com"

page = requests.get(url)  # get request from to that url
print(page)
# print(page.text)

soup = BeautifulSoup(page.text, "html.parser")
print(soup)

# findAll function to grab a list
# search for tagnames, attributes(kwargs), css class, text strings

# by tagname
titles = soup.findAll(name="title")
print(titles)  # list
print(titles[0])  # just the tag
print(titles[0].text)  # text inside the tag

# by attribute
keywords = soup.findAll(itemprop="keywords")
for word in keywords:
    print(word.text)

print("\n" * 10)
# by css class
quotes = soup.findAll(class_="quote")

for quote in quotes:
    print(quote)

print("\n" * 10)
print(quotes[0].prettify())

# by combinations
quotes = soup.findAll("span", class_="text")

for quote in quotes:
    print(quote.text)

quote_list = [x.text for x in quotes]
print(quote_list)

# by text
einsteins = soup.findAll(text="Albert Einstein")
for e in einsteins:
    print(e)

# find authors
authors = soup.findAll("small", class_="author")
print(authors[0].text)
author_list = [x.text.strip() for x in authors]

# print all my quotes
for i in range(len(quote_list)):
    print()
    print(quote_list[i])
    print("\t-", author_list[i])
