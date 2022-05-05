from requests_html import HTML, HTMLSession 
from Parser import ItemFilter
from Tester import TestPrintContents, TestTotalTraversing

"""Description:
This project use reuqests-html open source to parsing etsy 
Result will be the urls of items that user input
"""


"""Main Section"""
test_url = 'https://www.etsy.com/c/home-and-living?ref=catnav-891'
session = HTMLSession()
r = session.get(test_url)

# Find all <p> tags
p_tags = r.html.find("p")

contents = r.html.find("a")

print(contents)

##TestPrintContents(contents)


""" Test Single Item """
# print(len(extracted_cards))
# print()
# print(str(extracted_cards[18]))
# print()
# print(extracted_cards[18].attrs['class'][0] == "listing-link")      # access class by attrs['class'][idx_class1][idx_class2]
# print()
# print(extracted_cards[18].attrs['href'])



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