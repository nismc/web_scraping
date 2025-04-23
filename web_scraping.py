from bs4 import BeautifulSoup
import requests

url = "http://quotes.toscrape.com/"
response = requests.get(url)
html = response.text
soup = BeautifulSoup(html, "html.parser")

quotes = soup.find_all("div", class_="quote")

for quote in quotes:
    text = quote.find("span", class_="text").text
    author = quote.find("small", class_="author").text
    print(f"Quote: {text}")
    print(f"Author: {author}\n")
git push -u origin main