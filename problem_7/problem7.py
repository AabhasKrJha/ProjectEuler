# 10001st prime

# By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.
# What is the 10 001st prime number?

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

    for p in range(2, n+1):
        if prime[p]:
            primes.append(p)

    return primes

n = 1000001
primes = SieveOfEratosthenes(n)
print(primes[10000])