from collections import Counter

def num_words(string):
#    for word in str.split(" "):
    return Counter(string.split())

print(num_words("Vini, Vidi, Vici."))
print(num_words("Hello, world!"))
print(num_words("HeyDavidwhyaren'ttherespacesinthissentence"))
