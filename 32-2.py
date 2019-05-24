myOtherVariable = 1   #Insert lines below here
try:
  result = 10 // myVar
  print(result)
except ZeroDivisionError:        #This line has changed!
  print("An error occurred!")
print("Done!")
