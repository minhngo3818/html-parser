def _item_filter_(result_links) -> list:
  result = []
  
  for link in result_links:
    if 'class' in link.attrs.key():
      if link.attrs['class'][0] == "listing-link":
        result.append(str(link.attrs['href']))
    else:
      print("Key: \'class\' does not exist!", '\n')
      
  return result

def _print_items_(result):
  for item in result:
    print(item, '\n')
  
  
  
