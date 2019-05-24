cut = "Emerald"
clarity = "VS"
color = "E"
carat = 1.1
budget = 500
preferred_cuts = ["Emerald", "Cushion", "Princess", "Oval"]

#You may modify the lines of code above, but don't move them!
#When you Submit your code, we'll change these lines to
#assign different values to the variables.

#Diamonds are typically evaluated according to four aspects:
# - Cut: The way the diamond is cut
# - Clarity: How clear or flawless the diamond is, rated
#   as F (the best), IF, VVS, VS, SI, or I (the worst)
# - Color: How colorless the diamond is, rated from "D" (the
#   best) to "Z" (the worst)
# - Carat: How large the diamond is, weighed in carats
#
#Cut is usually a matter of personal preference. Clarity,
#color, and carat are matters of value: the clearer, more
#colorless, and larger a diamond is, the greater its value.
#
#Imagine you're shopping for a diamond. You have your
#preferred cuts, and you have a budget in mind. You're shown
#a diamond whose characteristics are represented by the cut,
#color, clarity, and carat variables above. You'll buy the
#diamond if its cost is less than your budget, and if its
#cut is one of your preferred cuts.
#
#At this store, every diamond has a base cost of 100.
#
#For every color rating worse than "D", the cost decreases by
#2%. An "F" color diamond would be worth 0.96 * the diamond
#cost otherwise because "F" is two colors worse than "D".
#
#A diamond's value is doubled for every level of clarity above
#I. A "VVS"-clarity diamond is worth 8 * the diamond cost
#otherwise because "VVS" is three levels higher than I, and
#doubling its value three times raises its value by 8x total.
#
#After finding its price based on color and clarity, its price
#is multiplied by its weight in carats.
#
#Your program should print "I'll take it!" if you will buy the
#diamond, "No thanks" if you will not. To purchase it, its price
#must be less than your budget and its cut must be one of your
#preferred cuts.
#
#HINT: You can find the number of characters between two
#characters by using the ord() function. ord("E") - ord("D")
#is 1; ord("Z") - ord("D") is 22.
#
#HINT 2: We haven't covered lists, but we did cover how to
#see if an item is present in a list using the 'in' operator
#in chapter 2.3.


#Add your code here!
'''
 I   SI  VS  VVS  IF   F
 *1  *2  *4  *8   *16  *32

 [I,   SI,  VS,  VVS,  IF,   F]
 [0,   1,   2,   3,    4,    5]
 *1   *2   *4   *8    *16   *32

 1  = 2^0 =(python) 2**0
 2  = 2^1 =(python) 2**1
 4  = 2^2 =(python) 2**2
 8  = 2^3 =(python) 2**3
 16 = 2^4 =(python) 2**4
 32 = 2^5 =(python) 2**5

 Array = ["I", "SI","VS", "VVS","IF","F"]
 Array.index("I")
 0
 Array.index("F")
 5
 '''
base_cost = 100

claritys = ["I", "SI", "VS", "VVS", "IF", "F"]

#print(clarity, claritys.index(clarity))   

clarity_cost = 2**claritys.index(clarity)

color_cost = 1

if ord(color) > ord("D"):
    color_cost = 1-((ord(color) - ord("D"))* 0.02)
    
price = base_cost * clarity_cost * color_cost * carat

#print(price)

if cut in preferred_cuts and price < budget:
    print("I'll take it!")
else:
    print("No thanks")
