myDictionary = {'Cinderella':'blue', 'Belle':'yellow', 'Mulan':'red', 'Tiana':'green', 'Rapunzel':'purple'}

for (princessName, princessDress) in myDictionary.items():
  print(princessName, "wears", princessDress)
  
for princessName in myDictionary:
  print(princessName, "wears", princessDress)
  
for princessName in myDictionary:
  print(princessName, "wears", myDictionary[princessName])

