"""Description:
This project use reuqests-html open source to parsing etsy 
Result will be the urls of items that user input
"""

from requests_html import HTML, HTMLSession 
from parser import getItemUrl, getContents
from tester import printContents

"""Main Section"""
test_url = 'https://www.etsy.com/c/home-and-living?ref=catnav-891'
session = HTMLSession()
r = session.get(test_url)

contents = getContents(r)

items_by_url = getItemUrl(contents)

# On process tesing a single item on find 3 crucial elements
items_by_li = r.html.find("#content", first=True).find("search-listting-group", first=True)


""" Test Section"""
# print(r.html) # -> return a HTML object contain url
# print(items_by_url)
# printContents(items_by_url)
print(items_by_li) # --> currently failed







# ------------------------ Experiment Section ---------------------------------#

# Test single element before implementation
# extracted_cards = contents
# print("number of elements: ",len(extracted_cards))
# print()
# print("print dictionary of attrs: ", str(extracted_cards[18].attrs))
# print()
# print("Key of attrs ", extracted_cards[18].attrs.keys())
# print()
# print("Check if listing-link: ", extracted_cards[18].attrs['class'][0] == "listing-link")      # access class by attrs['class'][idx_class1][idx_class2]
# print()
# print("Expected URL: ", extracted_cards[18].attrs['href'])
# print()


# Find all <p> tags
# p_tags = r.html.find("p")

# list_items = r.html.find('p')   # return a list
# # access syntax tag .class-name

# abs_links = r.html.absolute_links        # return a set
# # a set = r.html.links                    get links without full url in case of sub items

# div_content = r.html.find('div#content')     # return initial div tag with id='content' 

# links_content = r.html.find('#content', first=True)     # Add first=True to get the first element -> allow to access as html
# #print(links_content.tag)   return the found tag  

# extracted_cards = links_content.find('a')       # return a list

# # _test_print_contents_(extracted_cards)

# #result = _item_filter_(extracted_cards)

# #_test_complete_traversing_(result, extracted_cards)
# #_print_items_(extracted_cards)