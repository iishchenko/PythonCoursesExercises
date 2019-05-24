item = "quesadilla"
meat = "steak"
queso = False
guacamole = False
double_meat = False

if item == "quesadilla":
    print("Add 4.0 quesadilla")
    base_price = 4.0
elif item == "nachos":
    print("Add 4.50 nachos")
    base_price = 4.50
elif item == "burrito":
    print("Add 5.00 burrito")
    base_price = 5.0
    
if meat == "steak" or meat == "pork":
    print("Add 0.50 steak or pork")
    base_price += 0.50
    
if guacamole:
    print("Add 1.0 guacamole")
    base_price += 1.0

if queso and not "nachos":
    print("Add 1.0 queso and not nachos")
    base_price += 1.0

if double_meat and (meat == "steak" or meat == "pork"):
    print("Add 1.5 double_meat and steak or pork")
    base_price += 1.5
elif double_meat:
    print("Add 1.0 double_meat")
    base_price += 1.0
    
print(base_price)
