#The Collatz conjecture describes a sequence: starting with a positive number, if the number if even, halve it. If the number is odd, triple it and and add 1. Repeat. This sequence will always eventually reach 1, and should then stop. For example, if we started with 17:

#17 → 52 → 26 → 13 → 40 → 20 → 10 → 5 → 16 → 8 → 4 → 2 → 1

#The Collatz conjecture can be implemented recursively. Select the code below that could fill in the blank on line 6 so that this code will print every number in a Collatz sequence until it reaches 1, and then stop printing numbers after that.



def collatz(current_number):
    print(current_number)
    if current_number % 2 == 0:
        return collatz(current_number // 2)
    else:
        if current_number != 1:
            return collatz(current_number * 3 + 1)

print(collatz(17))
