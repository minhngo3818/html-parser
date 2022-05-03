from bs4 import BeautifulSoup
from requests_html import HTML, HTMLSession 


dummy_url = 'https://www.etsy.com/c/home-and-living?ref=catnav-891'

test_url = 'https://www.etsy.com/c/home-and-living?ref=catnav-891'

session = HTMLSession()

r = session.get(test_url)

list_items = r.html.find('p')   # return a list
# access syntax tag .class-name

abs_links = r.html.absolute_links        # return a set
# a set = r.html.links                    get links without full url in case of sub items

div_content = r.html.find('div#content')     # return initial div tag with id='content' 

links_content = r.html.find('#content', first=True)     # Add first=True to get the first element -> allow to access as html
#print(links_content.tag)   return the found tag  

extracted_cards = links_content.find('a')       # return a list
