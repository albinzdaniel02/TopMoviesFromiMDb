import bs4
import requests
URL="https://www.imdb.com/chart/top/"
page=requests.get(URL)
html=page.text
