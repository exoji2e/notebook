class SegmentTree:
    def __init__(self, arr, func=min):
        self.sz = len(arr)
        assert self.sz > 0
        self.func = func
        sz4 = self.sz*4
        self.L, self.R = [None]*sz4, [None]*sz4
        self.value = [None]*sz4
        def setup(i, lo, hi):
            self.L[i], self.R[i] = lo, hi
            if lo == hi:
                self.value[i] = arr[lo]
                return
            mid = (lo + hi)//2
            setup(2*i, lo, mid)
            setup(2*i + 1, mid+1, hi)
            self._fix(i)
        setup(1, 0, self.sz-1)

    def _fix(self, i):
        self.value[i] = self.func(self.value[2*i], self.value[2*i+1])

    def _combine(self, a, b):
        if a is None: return b
        if b is None: return a
        return self.func(a, b)

    def query(self, lo, hi):
        assert 0 <= lo <= hi < self.sz
        def _query(i, lo, hi):
            l, r = self.L[i], self.R[i]
            if r < lo or hi < l:
                return None
            if lo <= l <= r <= hi:
                return self.value[i]
            return self._combine(
                _query(i*2, lo, hi), 
                _query(i*2 + 1, lo, hi)
                )
        return _query(1, lo, hi)
    

    def assign(self, pos, value):
        assert 0 <= pos < self.sz
        def _assign(i, pos, value):
            l, r = self.L[i], self.R[i]
            if pos < l or r < pos: return
            if pos == l == r:
                self.value[i] = value
                return
            _assign(i*2, pos, value)
            _assign(i*2 + 1, pos, value)
            self._fix(i)
        return _assign(1, pos, value)


    def inc(self, pos, delta):
        assert 0 <= pos < self.sz
        def _inc(i, pos, delta):
            l, r = self.L[i], self.R[i]
            if pos < l or r < pos: return
            if pos == l == r:
                self.value[i] += delta
                return
            _inc(i*2, pos, delta)
            _inc(i*2 + 1, pos, delta)
            self._fix(i)
        _inc(1, pos, delta)



if __name__ == '__main__':
    def test(a, b):
        if a != b:
            print('failed:', a, b)
    t = SegmentTree([1, 2, 3])
    test(1, t.query(0, 2))
    t2 = SegmentTree([4, 3, 2, 1], func=lambda x, y: x + y)
    test(7, t2.query(0, 1))
    t2.assign(1, 10)
    test(14, t2.query(0, 1))
    t2.inc(2, 1)
    test(17, t2.query(0, 2))

    for i in range(1, 1000): # test that all sizes can be built!
        try: 
            t = SegmentTree([0]*i)
        except:
            print(i, 'Failed')
