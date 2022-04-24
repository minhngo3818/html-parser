from bs4 import BeautifulSoup
from requests_html import HTML, HTMLSession 


dummy_url = 'https://www.amazon.com/s?k=laptop&crid=199AKFS927SCF&sprefix=laptop%2Caps%2C131&ref=nb_sb_noss_1'

session = HTMLSession()
r = session.get(dummy_url)

div = r.html.find('div data-asin', first=True)

print(div.html)