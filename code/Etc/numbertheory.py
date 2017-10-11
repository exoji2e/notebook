def gcd(a, b):
    return b if a%b == 0 else gcd(b, a%b)

# returns g = gcd(a, b), x0, y0, where g = x0*a + y0*b
def xgcd(a, b):
    x0, x1, y0, y1 = 1, 0, 0, 1
    while b != 0:
        q, a, n = a // b, b, a % b
        x0, x1 = x1, x0 - q * x1
        y0, y1 = y1, y0 - q * y1
    return  a, x0, y0
