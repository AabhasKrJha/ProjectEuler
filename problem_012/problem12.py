# Highly divisible triangular number

# The sequence of triangle numbers is generated by adding the natural numbers. So the 7th triangle number would be 
# 1 + 2 + 3 + 4 + 5 + 6 + 7 = 28. The first ten terms would be:
# 1, 3, 6, 10, 15, 21, 28, 36, 45, 55, ...

# Let us list the factors of the first seven triangle numbers:
#      1: 1
#      3: 1,3
#      6: 1,2,3,6
#     10: 1,2,5,10
#     15: 1,3,5,15
#     21: 1,3,7,21
#     28: 1,2,4,7,14,28

# We can see that 28 is the first triangle number to have over five divisors.
# What is the value of the first triangle number to have over five hundred divisors?

def HighlyDivisibleTriangularNumber(num):
    factor_count = 0
    for divisor in range(1, int(num/2) + 1):
        if num % divisor == 0:
            factor_count += 1
    if factor_count > 500:
        return True
    else:
        return False

found = False
num = 1
while not found:
    
    triangular_num = int(num * (num + 1) / 2)
    print(f"NAh {num} : ", triangular_num)
    if HighlyDivisibleTriangularNumber(triangular_num):
        print(triangular_num)
        found = True
    num += 1
