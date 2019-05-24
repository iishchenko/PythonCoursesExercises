current_hour = 12
current_minute = 37
current_section = "PM"
due_hour = 9
due_minute = 0
due_section = "AM"

current_time = str(current_hour) + ":" + str(current_minute) + " " + str(current_section)
print(current_time)

due_time = str(due_hour) + ":" + str(due_minute) + " " + str(due_section)
print(due_time)

current_hour = 12
current_minute = 37
current_section = "AM"
due_hour = 9
due_minute = 0
due_section = "AM"

if current_hour = 12 and current_section = "AM":
   current_hour = 0
else: 
   current_hour
   
if duet_hour = 12 and due_section = "AM":
   current_hour = 0
else:
   current_hour
  
if current_section >= due_section and current_hour >= due_hour and current_minute >= due_minute:
   print ("True")
else:
   print("False")

if current_section > due_section:
    print(False)
elif current_hour > due_hour:
    print(False)
elif current_minute > due_minute:
    print(False)
else:
    print(True)
