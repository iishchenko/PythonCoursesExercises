my_file = open("my_file.txt")
sum = 0
count = 0
for num in my_file:
    sum += num
    count += 1
print(sum / count)
my_file.close()
