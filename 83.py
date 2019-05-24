classes = {"Math" : ["David", "Lucy", "Dana"],
           "Physics" : ["Addison", "Vrushali", "Bilbo"],
           "Chemistry" : ["Sara", "Lugos", "Mireia", "Perle"],
           "Computing" : ["Partha", "Venijamin", "Terra", "Sofia"],
           "History" : ["Tryphon", "Gevorg", "Raza", "Rein"]}

print("Students in Computing:", classes["Computing"])
#Add Francis to History
classes["History"].append("Francis")    
print("Students in History:", classes["History"])



addressBook = {"David": ("555 Home St", "4045551234", "david@david.com"),
               "Lucy" : ("555 Home St", "4045555678", "lucy@lucy.com"),
               "Dana" : ("123 There Rd", "4045559101", "dana@dana.net")}

print("David's Information:", addressBook["David"])
print("Dana's Phone Number:", addressBook["Dana"][1])



addressBook = {"David": {"address" : "555 Home St", "phone" : "4045551234", 
                          "email" : "david@david.com"},
               "Lucy" : {"address" : "555 Home St", "phone" : "4045555678", 
                         "email" : "lucy@lucy.com"},
               "Dana" : {"address" : "123 Here Rd", "phone" : "4045559101", 
                         "email" : "dana@dana.net"}}

print("David's Information:", addressBook["David"])
print("Dana's Phone Number:", addressBook["Dana"]["phone"])

