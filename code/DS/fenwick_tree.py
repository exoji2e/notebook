# Tested on: https://open.kattis.com/problems/froshweek
class FenwickTree: # zero indexed calls!
    def __init__(self, sz):
        self.data = [0]*(sz+1)
    def inc(self, i, delta):
        i += 1 # (to 1 indexing)
        while i < len(self.data):
            self.data[i] += delta
            i += i&-i # lowest oneBit
    def sum(self, i):
        i += 1 # (to 1 indexing)
        S = 0
        while i > 0:
            S += self.data[i]
            i -= i&-i
        return S
    def query(self, lo, hi):
        return self.sum(hi) - self.sum(lo)