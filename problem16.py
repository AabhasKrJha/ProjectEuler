# Power digit sum

# 215 = 32768 and the sum of its digits is 3 + 2 + 7 + 6 + 8 = 26.
# What is the sum of the digits of the number 21000?

def power_digit_sum(num):

    sum = 0
    str_num =list(str(num))
    for n in str_num:
        sum += int(n)
    
    print(sum)

power_digit_sum(2**1000)