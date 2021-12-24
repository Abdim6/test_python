
import requests
from bs4 import BeautifulSoup
url = "https://www.gov.uk/search/news-and-communications"
page = requests.get(url)
soup = BeautifulSoup(page.content, 'html.parser')
donnee = soup.title.string
# balise_a = soup.find_all(id="")
titres = soup.find_all("a", class_="gem-c-document-list__item-title")
# print(titres)
for title in titres:
    print(title.string)