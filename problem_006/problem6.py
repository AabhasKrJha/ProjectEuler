# Sum square difference

# The sum of the squares of the first ten natural numbers is,
# 1^2 + 2^2 + ........ + 10^2 = 385
# The square of the sum of the first ten natural numbers is,
# (1 + 2 + ....... + 10)^2 = 55^2 = 3025
# Hence the difference between the sum of the squares of the first ten natural numbers and the square of the sum is
# 3025 - 385 = 2640.
# Find the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum.

def sum_square_difference():

    # sqaure of sum
    sum = 100 * (100 + 1) / 2
    sq_sum = sum ** 2 

    # sum of squares
    sum_sq = 0
    for n in range(1, 101):
        sum_sq += n ** 2
    
    print(abs(sq_sum - sum_sq))

sum_square_difference()