#Above is an alternate implementation of the Collatz conjecture described in 
#the previous problem part. Select the code below that could fill in the blank on 
#line 8 so that this code will print every number in a Collatz sequence until it reaches 1, 
#and then stop printing numbers after that.

def collatz(current_number):
    print(current_number)
    if current_number % 2 == 0:
      return collatz(current_number // 2)
    elif current_number % 2 == 1:
      return collatz(current_number * 3 + 1)
    else:
      return 1
      
      

print(collatz(17))
