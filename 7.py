
mystery_string = "zizazzle"

counter = 0
counter_2 = 0
counter_3 = 0

for num in range(len(mystery_string)):
  if "z" in mystery_string[num]:
    counter += 1

found = "zz" in mystery_string
if found == True:
    counter_2 += 1

found = "zzz" in mystery_string
if found == True:
    counter_3 += 1
  

if counter_3 >= 1:
  print("I'm sleepy...")
elif counter_2 >= 1:
  print("I love ZZ Top!")
elif counter >= 1:
  print("One is the loneliest number.")
else: 
  print("Who needs z anyway?")
  
print(counter)
print(counter_2)
print(counter_3)
