# Largest palindrome product

# A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers is 
# 9009 = 91 × 99.
# Find the largest palindrome made from the product of two 3-digit numbers.

def largest_pallindrome_product():
     
    pallindromes = list()

    def is_pallindrome(num):
        return num == num[::-1]

    lower_range = 100
    upper_range = 999

    for i in range(lower_range, upper_range + 1):
        for j in range(lower_range, upper_range + 1):
            product = i * j
            if is_pallindrome(str(product)):
                pallindromes.append(product)
    
    pallindromes.sort()
    return pallindromes[-1]
    
print(largest_pallindrome_product())
