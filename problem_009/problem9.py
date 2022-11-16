# Special Pythagorean triplet

# A Pythagorean triplet is a set of three natural numbers, a < b < c, for which,
# a^2 + b^2 = c^2
# For example, 32 + 42 = 9 + 16 = 25 = 52.
# There exists exactly one Pythagorean triplet for which a + b + c = 1000.
# Find the product abc.

## PYTHON CODE TAKES MORE THAN 3 MINUTES TO FIND THE PRODUCT.
## C CODE TAKES AROUND 10 SECONDS
## CPP IS EVEN FASTER THAN C TAKES 2-3 SECONDS LESS THAN THE C CODE.
## JAVA IS FASTER THAN CPP RUNS IN AN INSTANT.

def SpecialPythagoreanTriplet():

    def isTriplet(a, b, c):
        if (a**2 + b**2 == c**2):
            return True
        return False
    
    def isTriangle(a, b, c):
        if (a + b > c) and (a + c > b) and (b + c > a):
            return True
        return False

    for a in range(1, 1001):
        for b in range(1, 1001):
            for c in range(1, 1001):
                if isTriplet(a, b, c) and isTriangle(a, b, c) and (a + b + c == 1000):
                    return a*b*c

print(SpecialPythagoreanTriplet())