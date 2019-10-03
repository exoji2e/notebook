def gcd(a, b):
  return b if a%b == 0 else gcd(b, a%b)

# returns g = gcd(a, b), x0, y0, 
# where g = x0*a + y0*b
def xgcd(a, b):
  x0, x1, y0, y1 = 1, 0, 0, 1
  while b != 0:
    q, a, b = (a // b, b, a % b)
    x0, x1 = (x1, x0 - q * x1)
    y0, y1 = (y1, y0 - q * y1)
  return (a, x0, y0)

def crt(la, ln):
    assert len(la) == len(ln)
    for i in range(len(la)):
        assert 0 <= la[i] < ln[i]
    prod = 1
    for n in ln:
        assert gcd(prod, n) == 1
        prod *= n
    lN = []
    for n in ln:
        lN.append(prod//n)
    x = 0
    for i, a in enumerate(la):
        print(lN[i], ln[i])
        _, Mi, mi = xgcd(lN[i], ln[i])
        x += a*Mi*lN[i]
    return x % prod

# finds x^e mod m
def modpow(x, m, e):
    res = 1
    while e:
        if e%2 == 1:
            res = (res*x) % m
        x = (x*x) % m
        e = e//2
    return res

# Divides a list of digits with an int.
# A lot faster than using bigint-division.
def div(L, d):
  r = [0]*(len(L) + 1)
  q = [0]*len(L)
  for i in range(len(L)):
    x = int(L[i]) + r[i]*10
    q[i] = x//d
    r[i+1] = x-q[i]*d
  s = []
  for i in range(len(L) - 1, 0, -1):
    s.append(q[i]%10)
    q[i-1] += q[i]//10

  while q[0]:
    s.append(q[0]%10)
    q[0] = q[0]//10
  s = s[::-1]
  i = 0
  while s[i] == 0:
    i += 1
  return s[i:]


# Multiplies a list of digits with an int.
# A lot faster than using bigint-multiplication.
def mul(L, d):
  r = [d*x for x in L]
  s = []
  for i in range(len(r) - 1, 0, -1):
    s.append(r[i]%10)
    r[i-1] += r[i]//10
  while r[0]:
    s.append(r[0]%10)
    r[0] = r[0]//10
  return s[::-1]

large_primes = [
5915587277,
1500450271,
3267000013,
5754853343,
4093082899,
9576890767,
3628273133,
2860486313,
5463458053,
3367900313,
10000000000000061,
10**16 + 61,
10**17 + 3
        ]

