def testTotalTraversing(result, raw_parsed_output):
  if len(result) == len(raw_parsed_output):
    print('Traversed all items checked!', '\n')
  else:
    print('Funtion did not go through!', '\n')

# Print items in the list
def printContents(parsed_list):
  for item in parsed_list:
    print(item, '\n')

  print('\n#### Process Ended ####\n')
