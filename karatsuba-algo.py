# KARATSUBA algorithm is a divide and conquer algorithm recursively that: 
# - takes two large nums you want to multiply and instead of using long multiplication it -
# - uses divide and conquer approuch to speed up the multiplication time

# Karatsuba works by: 
# 1. DIVIDE each number in to two smaller parts (ex. 1248 is 12 & 48 // 5678 is 56 & 78)
# 2. CONQUER by multiplying the smaller parts together (12*56, 12*78, 56*12, 56*48)
# 3. COMBINE: then combine the products to get final result 

def karatsubaMultiplication(x ,y):
    """Multiply two integers using Karatsuba's algorithm."""
    #convert to strings for easy access to digits
    x = str(x)
    y = str(y)
    #base case for recursion
    if len(x) == 1 and len(y) == 1:
        return int(x) * int(y)
    if len(x) < len(y):
        x = zeroPad(x, len(y) - len(x))
    elif len(y) < len(x):
        y = zeroPad(y, len(x) - len(y))
    n = len(x)
    j = n//2
    #for odd digit integers
    if (n % 2) != 0:
        j += 1    
    BZeroPadding = n - j
    AZeroPadding = BZeroPadding * 2
    a = int(x[:j])
    b = int(x[j:])
    c = int(y[:j])
    d = int(y[j:])
    #recursively calculate
    ac = karatsubaMultiplication(a, c)
    bd = karatsubaMultiplication(b, d)
    k = karatsubaMultiplication(a + b, c + d)
    A = int(zeroPad(str(ac), AZeroPadding, False))
    B = int(zeroPad(str(k - ac - bd), BZeroPadding, False))
    return A + B + bd

    