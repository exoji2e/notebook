# Tested on: https://open.kattis.com/problems/froshweek
class FenwickTree: # zero indexed calls!
    # Give array or size!
    def __init__(self, sz):
        if type(sz) == int:
            self.data = [0]*(sz+1)
        elif type(sz) == list:
            A = sz
            self.data = [0]*(len(A) + 1)
            for i, a in enumerate(A):
                self.inc(i, a)
    # A[i] = v
    def assign(self, i, v):
        currV = self.query(i, i)
        self.inc(i, v - currV)
    # A[i] += v
    def inc(self, i, delta):
        i += 1 # (to 1 indexing)
        while i < len(self.data):
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

if __name__ == '__main__':
    tree = FenwickTree(10)
    tree.assign(0, 5)
    tree.assign(1, 4)
    assert tree.query(0, 1) == 9
    t2 = FenwickTree([1, 2, 3, 4])
    assert t2.query(1, 3) == 9