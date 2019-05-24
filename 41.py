start = 0
finish = 10

for i in range(start, finish, 2):
    print(i)

for i in range(start, finish + 1, 2):
    print(i)

for i in range(start + 1, finish, 2):
    print(i)

while start <= finish:
    print(start)
    start += 2
 
while start < finish:
    print(start)
    start += 2
 
while start <= finish:
    start += 2
    print(start)
 
while start < finish:
    start += 2
    print(start)
