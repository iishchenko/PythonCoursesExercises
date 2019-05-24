try:
  print(undeclaredVariable)     #This line causes a NameError
  print(1 / 0)                  #This line causes a ZeroDivisionError
  print("No error occurred!")
except NameError:
  print("A NameError occurred!")
except ZeroDivisionError:
  print("A ZeroDivisionError occurred!")
print("Done!")
