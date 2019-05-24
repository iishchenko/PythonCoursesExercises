#Insert lines below here

myOtherVar = 1

try:
  result = 10 // myVar
  print(result)
except (ZeroDivisionError, TypeError):
  print("An expected error occurred!")
else:
  print("No errors occurred!")
finally:
  print("Closing down...")
print("Done!")
