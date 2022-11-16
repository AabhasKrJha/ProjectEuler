# Smallest multiple

# 2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.
# What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?

import timeit
# import time

def lcm(x, y):
    num = 1
    while True:
        if num%x == 0 and num%y == 0:
            return num
        else:
            num += 1

def smallest_multiple_method_one():
    # faster than method 2 by 4 seconds
    LCM = lcm(1, 2)
    for i in range(3, 21):
        LCM = lcm(LCM, i)
    return LCM

def smallest_multiple_method_two():

    divisors = [2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
    divident = 1

    while True:
        divisible = True
        for divisor in divisors:
            if divident % divisor != 0:
                divisible = False
                break
        if divisible:
            return divident
        else:
            divident += 1

smallest_multiple = smallest_multiple_method_one

# start1 = time.perf_counter()
# print(smallest_multiple())
# finish1 = time.perf_counter()

# start2 = time.perf_counter()
# smallest_multiple_method_two()
# finish2 = time.perf_counter()

# print("METHOD 1 -> ", finish1 - start1)
# print("METHOD2 -> ", finish2 - start2)

print(smallest_multiple_method_two())

def main():
    print("METHOD 1 : ", timeit.timeit(smallest_multiple_method_one, number=1))
    print("METHOD 2 : ", timeit.timeit(smallest_multiple_method_two, number=1))

main()