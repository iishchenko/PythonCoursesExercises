can_afford = True
destination_is_safe = True
educational_value = False
relatives_nearby = False
is_international = True
have_passport = True
afraid_to_fly = False
is_warm = True 
is_a_beach = True
have_a_car = True 
has_attraction = False 
is_a_city = False 
is_off_peak = False 
has_skiing = False 
is_warm = True

parents_will_agree = destination_is_safe and (educational_value or relatives_nearby)

if parents_will_agree:
   print("parents_will_agree: True")
else:
   print("parents_will_agree: False")

able_to_go = (is_international and have_passport and not afraid_to_fly) or (not is_international and (have_a_car or not afraid_to_fly))

if able_to_go:
   print("able_to_go: True")
else:
   print("able_to_go: False")

locations_conditions = (is_a_beach and is_warm) or (has_skiing and not is_warm) or (is_a_city and is_off_peak) or (is_a_city and has_attraction)

if locations_conditions:
    print ("locations_conditions: True")
else:
   print("locations_conditions: False")

if able_to_go and locations_conditions and ((can_afford and destination_is_safe) or (parents_will_agree)):
   print ("True")
else:
   print("False")
