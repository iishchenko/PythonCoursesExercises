story = "A"
text = "B"
role = "C"
director = "D"
cast = "F"

counter = 0

if story == "A":
    counter +=6
if story == "B":
    counter +=5
if story == "C":
    counter +=4
if story == "D":
    counter +=2
    
if text == "A":
    counter +=5
if text == "B":
    counter +=4
if text == "C":
    counter +=3
if text == "D":
    counter +=1

if role == "A":
    counter +=4
if role == "B":
    counter +=3
if role == "C":
    counter +=2
if role == "D":
    counter +=1

if director == "A":
    counter +=3
if director == "B":
    counter +=2
if director == "C":
    counter +=1

if cast == "A":
    counter +=2
if cast == "B":
    counter +=1

if counter == 20:
  print("Perfect score")
elif counter <= 19 and counter >=17:
  print("Must do")
elif counter <= 16 and counter >=14:
  print("Seriously consider")
elif counter <= 13 and counter >=12:
  print("On the bubble")
else:
  print("Pass")


