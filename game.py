low = 0
high = 100

print("Please think of a number between " + str(low)+ " and " + str(high) + "!")
option_keyboard =  ' ' 

while option_keyboard != 'c':
  guess_value = (high + low) // 2   # value to guess
  print("Is your secret number " + str(guess_value) + "?")

  # Read a value from the keyboard:
  option_keyboard = input("Enter 'h' to indicate the guess is too high. Enter 'l' to indicate the guess is too low. Enter 'c' to indicate I guessed correctly. ")

  if option_keyboard == 'l':    # low -> you have to change the limit on the top
	  low = guess_value
  elif option_keyboard == 'h':
  	 high = guess_value
  elif option_keyboard == 'c':
	  print ("Game over. Your secret number was: " + str(guess_value))
  else:
  	  print ("Sorry, I did not understand your input.")



