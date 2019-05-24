
def merge_strings(first, second, reverse = False, capitalize = True):
  result = ""
  if reverse == False:
    result = first + second
  else:
    result = second + first
  
  if capitalize == True:
    result = result.upper()
  
  print(result)
  

merge_strings("carrot", "turnip", reverse = True) 
merge_strings("lettuce", "tomato", capitalize = False)
merge_strings("onion", "raisin")
