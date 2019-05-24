minimum = 5
maximum = 14
even = False

#You may modify the lines of code above, but don't move them!
#When you Submit your code, we'll change these lines to
#assign different values to the variables.
#
#Write a loop (we suggest a for loop) that prints the numbers
#from minimum to maximum, including minimum and maximum
#themselves. If even is True, print only the even numbers.
#If even is False, print only the odd numbers. You may assume
#minimum will always be less than maximum.
#
#With the initial values for minimum, maximum, and even above,
#this should print 6, 8, 10, 12, 14 -- each number would be on
#its own line, no commas.


#Add your code here!

is_min_even = (minimum % 2) == 0

if (even == True and is_min_even == False) or (even == False and is_min_even == True):
    # if it wants evens but minimum is odd, or if it wants odds but minimum is even, we must start in the next value
    minimum += 1

for i in range(minimum, maximum+1, 2):
    print(i)




#if even == True:
#    is_even = (minimum % 2) == 0
#    if is_even == False:
#       for i in range(minimum+1, maximum+1, 2):
#                print(i)
#    else:
#        for i in range(minimum, maximum+1, 2):
#               print(i)
#else:
#    is_even = (minimum % 2) == 0
#    if is_even == False:
#        for i in range(minimum, maximum+1, 2):
#                print(i)
#    else:
#        for i in range(minimum+1, maximum+1, 2):
#               print(i)
