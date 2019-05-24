#Insert lines below here
myOtherVariable = 1

try:
  result = 10 // myVar
  print(result)
except ZeroDivisionError:
  print("An ZeroDivisionError occurred!")
except NameError:
  print("A NameError occurred!")
except:
  print("Some other error occurred!")
print("Done!")
