from collections import *
def shortest_cycle(G):
    ''' Returns the length of shortest cycle even in an undirected graph. 
    Floyd Warshall only handles directed graphs, 
    but considers an undirected edge to be a cycle of length 2.
    G is adjacency list. '''
    n = len(G)
    ans = 10**18
    INF = 10**9
    for i in range(n):
        dist = [INF] * n
        par = [-1] * n
        dist[i] = 0
        q = deque()
        q.append(i)
        while q:
            x = q[0]
            q.popleft()
 
            for child in G[x]:
                if dist[child] == INF:
                    dist[child] = 1 + dist[x]
 
                    par[child] = x
                    q.append(child)
 
                elif par[x] != child and par[child] != x:
                    ans = min(ans, dist[x] +
                                   dist[child] + 1)
    return ans