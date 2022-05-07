# Return a list of Element objects 
def getContents(raw_parsed_data):
  return raw_parsed_data.html.find("#content", first=True).find('a')


def getCorrectCard(contents):
  result = []
  
  for link in contents:
    if ('class' in link.attrs.keys() and
      link.attrs['class'][0] == "listing-link"):
        result.append(str(link.attrs['href']))
      
  return result

  
  
  
