import requests
from bs4 import BeautifulSoup

r = requests.get("http://fantasy.premierleague.com/web/api/elements/100/")

soup = BeautifulSoup(r.content)

f = open("newfile.txt", "a", encoding="utf-8")

f.write(soup.prettify())

f.close()

print(soup.prettify())

