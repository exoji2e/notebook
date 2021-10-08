# S is index, G is adjacancy list
# finds distance from S to all verticies in G
def bfs(S, G):
    q = [S]
    INF = 10**18
    dist = [INF]*len(G)
    dist[S] = 0
    while q:
        q2 = []
        for u in q:
            for v in G[u]: 
                # early break here if only interesed in length of S -> T path.
                if dist[u] + 1 < dist[v]:
                    dist[v] = dist[u] + 1
                    q2.append(v)
        q = q2
    return dist