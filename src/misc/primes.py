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

def getPrimesBelow(N):
    primes = []
    soll = [1]*N
    for p in range(2, N):
        if soll[p]:
            primes.append(p)
            for k in range(p*p, N, p):
                soll[k] = 0
    return primes

def isPrime(N):
    if N < 2: return False
    if N%2 == 0: return N == 2
    mx = min(int(N**.5) + 2, N)
    for i in range(3, mx, 2):
        if N % i == 0: return False
    return True

def genPrimesFrom(N):
    while True:
        if isPrime(N):
            yield N
        N += 1

def getPrimesFrom(N, cnt):
    itr = genPrimesFrom(N)
    return [next(itr) for _ in range(cnt)]