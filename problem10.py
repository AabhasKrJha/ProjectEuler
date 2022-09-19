# Summation of primes

# The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.
# Find the sum of all the primes below two million.

def SieveOfEratosthenes(n):

    # Boolean array with 0 to n(inclusive) 
    prime = [True for _ in range(n + 1)]

    p = 2
    while (p * p < n):
        if prime[p] == True:
            # setting all the multiple from p^2 of p to be false
            for i in range(p*p, n, p):
                prime[i] = False
        p += 1
    
    primes = []

    for p in range(2, n):
        if prime[p]:
            primes.append(p)

    return primes

n = 2000000
print(sum(SieveOfEratosthenes(n)))