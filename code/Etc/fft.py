import cmath
# A has to be of length a power of 2.

def FFT(A, inverse=False):
    N = len(A)
    if N <= 1: 
        return A
    if inverse:
        D = FFT(A) # d_0/N, d_{N-1}/N, d_{N-2}/N, ...
        return map(lambda x: x/N, [D[0]] + D[:0:-1])
    evn = FFT(A[0::2])
    odd = FFT(A[1::2])
    Nh = N//2
    return [evn[k%Nh]+cmath.exp(2j*cmath.pi*k/N)*odd[k%Nh]
            for k in range(N)]

# A has to be of length a power of 2.
def FFT2(a, inverse=False):
    N = len(a)
    j = 0
    for i in range(1, N):
        bit = N>>1
        while j&bit:
            j ^= bit
            bit >>= 1
        j^= bit
        if i < j:
            a[i], a[j] = a[j], a[i]

    L = 2
    MUL = -1 if inverse else 1
    while L <= N:
        ang = 2j*cmath.pi/L * MUL
        wlen = cmath.exp(ang)
        for i in range(0, N, L):
            w = 1
            for j in range(L//2):
                u = a[i+j]
                v = a[i+j+L//2] * w
                a[i+j] = u + v
                a[i+j+L//2] = u - v
                w *= wlen
        L *= 2
    if inverse:
        for i in range(N):
            a[i] /= N
    return a

def uP(n):
    while n != (n&-n):
        n += n&-n
    return n

# C[x] = sum_{i=0..N}(A[x-i]*B[i])
def polymul(A, B):
    sz = max(uP(len(A), len(B)))
    A = A + [0]*(sz - len(A))
    B = B + [0]*(sz - len(B))
    fA = FFT(A)
    fB = FFT(B)
    fAB = [a*b for a, b in zip(fA, fB)]
    C = [x.real for x in FFT(fAB, True)]
    return C



