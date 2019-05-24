class ClockTime:
     def __init__(self, hour = 12, minute = 0, period = "AM"):
         self.hour = hour
         self.minute = minute
         self.period = period
         print(self.hour, self.minute, self.period)





new_time = ClockTime()
 
#new_time = ClockTime(self)
 
new_time = ClockTime(12)
 
#new_time = ClockTime(0)
 
#new_time = ClockTime("AM")
 
new_time = ClockTime(12, 0)
 
#new_time = ClockTime(12, "AM")
 
#new_time = ClockTime(0, "AM")
 
new_time = ClockTime(12, 0, "AM")
 
new_time = ClockTime(hour = 12)
 
new_time = ClockTime(minute = 0)
 
new_time = ClockTime(period = "AM")
 
new_time = ClockTime(hour = 12, minute = 0)
 
new_time = ClockTime(hour = 12, period = "AM")
 
new_time = ClockTime(minute = 0, period = "AM")
 
new_time = ClockTime(hour = 12, minute = 0, period = "AM")
