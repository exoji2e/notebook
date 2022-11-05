# Tested on: https://open.kattis.com/problems/froshweek
class FenwickTree: # zero indexed calls!
    # Give array or size!
    def __init__(self, blob):
        if type(blob) == int:
            self.sz = blob
            self.data = [0]*(blob+1)
        elif type(blob) == list:
            A = blob
            self.sz = len(A)
            self.data = [0]*(self.sz + 1)
            for i, a in enumerate(A):
                self.inc(i, a)
    # A[i] = v
    def assign(self, i, v):
        currV = self.query(i, i)
        self.inc(i, v - currV)
    # A[i] += delta
    # this method is ~3x faster than doing A[i] += delta
    def inc(self, i, delta):
        i += 1 # (to 1 indexing)
        while i <= self.sz:
            self.data[i] += delta
            i += i&-i # lowest oneBit
    # sum(A[:i+1])
    def sum(self, i):
        i += 1 # (to 1 indexing)
        S = 0
        while i > 0:
            S += self.data[i]
            i -= i&-i
        return S
    # return sum(A[lo:hi+1])
    def query(self, lo, hi):
        return self.sum(hi) - self.sum(lo-1)

    # for indexing - nice to have but not required
    def __fixslice__(self, k):
        return slice(k.start or 0, self.sz if k.stop == None else k.stop)
    def __setitem__(self, i, v):
        self.assign(i, v)
    def __getitem__(self, k):
        if type(k) == slice:
            k = self.__fixslice__(k)
            return self.query(k.start, k.stop - 1)
        elif type(k) == int:
            return self.query(k, k)
