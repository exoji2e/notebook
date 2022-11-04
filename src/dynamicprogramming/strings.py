def zfun(t):
    z = [0]*len(t)
    n = len(t)
    l, r = (0,0)
    for i in range(1,n):
        if i < r:
            z[i] = min(z[i-l], r-i+1)
        while z[i] + i < n and t[i+z[i]] == t[z[i]]:
            z[i]+=1
        if i + z[i] - 1 > r:
            l = i
            r = i + z[i] - 1
    return z

def matches(t, p):
    s = p + '#' + t
    return filter(lambda x: x[1] == len(p),
            enumerate(zfun(s)))

def boarders(s):
    b = [0]*len(s)
    for i in range(1, len(s)):
        k = b[i-1]
        while k>0 and s[k] != s[i]:
            k = b[k-1]
        if s[k] == s[i]:
            b[i] = k+1
    return b
