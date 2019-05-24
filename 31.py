for i in range(2, -3, -1):    #Counts down from 2 to -2: 2, 1, 0, -1, -2
  try:
    print(2 / i)    #Prints 2 divided by the current value of i
  except ZeroDivisionError:
    print("We can't divide by 0!")
