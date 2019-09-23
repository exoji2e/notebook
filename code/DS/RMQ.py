class RMQ:
    def __init__(self, arr, func=min):
        import math
        self.sz = len(arr)
        MAXN = self.sz
        LOGMAXN = int(math.ceil(math.log(MAXN + 1, 2)))
        self.data = [[0]*LOGMAXN for _ in range(MAXN)]
        for i in range(MAXN):
            self.data[i][0] = arr[i]
        for j in range(1, LOGMAXN):
            for i in range(MAXN - (1<<j)+1):
                self.data[i][j] = func(self.data[i][j-1], self.data[i + (1<<(j-1))][j-1])

    def query(self, a, b):
        if a > b:
            # some default value when query is empty
            return 1
        d = b - a + 1
        k = int(math.log(d, 2))
        return self.func(self.data[a][k], self.data[b - (1<<k) + 1][k])
