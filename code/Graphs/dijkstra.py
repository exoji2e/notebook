from heapq import heappop as pop, heappush as push
# adj: adj-list where edges are tuples (node_id, weight):
# (1) --2-- (0) --3-- (2) has the adj-list:
# adj = [[(1, 2), (2, 3)], [(0, 2)], [0, 3]]
def dijk(adj, S, T):
    N = len(adj)
    INF = 10**10
    dist = [INF]*N
    pq = []
    dist[S] = 0
    push(pq, (0, S))

    while pq:
        D, i = pop(pq)
        if D != dist[i]: continue
        for j, w in adj[i]:
            alt = D + w
            if dist[j] > alt:
                dist[j] = alt
                push(pq, (alt, j))
    
    return dist[T]
