# Longest Collatz sequence

# The following iterative sequence is defined for the set of positive integers:
# n → n/2 (n is even)
# n → 3n + 1 (n is odd)

# Using the rule above and starting with 13, we generate the following sequence:
# 13 → 40 → 20 → 10 → 5 → 16 → 8 → 4 → 2 → 1

# It can be seen that this sequence (starting at 13 and finishing at 1) contains 10 terms. Although it has not been proved yet (Collatz Problem), 
# it is thought that all starting numbers finish at 1.
# Which starting number, under one million, produces the longest chain?
# note: Once the chain starts the terms are allowed to go above one million.

max_term_count = 0
largest_starting_num = 1

def CollatzSequence(num):

    global largest_starting_num, max_term_count

    CollatzNum = num
    terms = 1
    sequence = [num]

    while num != 1:
        if num % 2 == 0:
            num = int(num/2)
        else:
            num = 3*num + 1
        terms += 1
        sequence.append(num)
    
    if terms > max_term_count:
        max_term_count = terms
        largest_starting_num = CollatzNum

for num in range(1, 1000000):
    CollatzSequence(num)

print(largest_starting_num)