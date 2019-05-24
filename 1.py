s = 'azcbobobegghaklbo'
numBob = 0

#print("range(len(s)) generates ", range(len(s)))
for pos in range( len(s) ):
    #print("pos is ", pos, ", s[pos] is ", s[pos])
    
    if s[pos] == 'b' and s[pos+1] == 'o' and s[pos+2] == 'b':
      numBob += 1

print('Number of times bob occurs is: ' + str(numBob))

'''for char in s:
    if char == 'b':
      print("char is ", char)
      numBob += 1'''
      

