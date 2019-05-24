hot = True
cold = False
rainy = True
windy = False
snowy = False

if cold or windy or rainy: 
    print("Jacket: True")
else:
    print("Jacket: False")
if cold or snowy or rainy: 
    print("Boots: True")
else:
    print("Boots: False")
if hot and not rainy: 
    print("Flip-Flops: True")
else:
    print("Flip-Flops: False")
if hot and not (rainy or windy): 
    print("T-shirt: True")
else: 
    print("T-shirt: False")
