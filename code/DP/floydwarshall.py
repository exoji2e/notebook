n, m = map(int, input().split())
INF = 1000000000
dist = [[INF]*n for _ in range(n)]
nxt = [[None]*n for _ in range(n)]
edgs = [tuple(map(int, input().split())) for _ in range(m)]
for e in edgs:
    dist[e[0]][e[1]] = e[2]
    nxt[e[0]][e[1]] = e[1]
for k in range(n):
    for i in range(n):
        for j in range(n):
            if dist[i][j] > dist[i][k] + dist[k][j]:
                dist[i][j] = dist[i][k] + dist[k][j]
                nxt[i][j] = nxt[i][k]
def path(i, j):
    if nxt[i][j] == None: return []
    path = [i]
    while i != j:
        i = nxt[i][j]
        path.append(i)
    return path
