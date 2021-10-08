# used on https://open.kattis.com/problems/arboriculture
# G is Bipartite graph N x M (N <= M) where [i][j] is cost to match L[i] and R[j]
# Ported from: https://raw.githubusercontent.com/kth-competitive-programming/kactl/main/content/graph/WeightedMatching.h
# Description: Given a weighted bipartite graph, matches every node on
# the left with a node on the right such that no
# nodes are in two matchings and the sum of the edge weights is minimal. Takes
# cost[N][M], where cost[i][j] = cost for L[i] to be matched with R[j] and
# Returns: (min cost, match), where L[i] is matched with R[match[i]]. 
# Negate costs for max cost.
# Time: O(N^2M)
#
def hungarian(G):
    INF = 10**18
    if len(G) == 0: 
        return 0, []
    
    n, m = len(G) + 1, len(G[0]) + 1
    u, v, p = [0]*n, [0]*m, [0]*m
    ans = [0]*(n-1)
    for i in range(1, n):
        p[0], j0 = i, 0
        dist, pre = [INF]*m, [-1]*m
        done = [False]*(m+1)
        while True:
            done[j0] = True
            i0, j1, delta = p[j0], 0, INF
            for j in range(1, m):
                if done[j]: continue
                cur = G[i0 - 1][j-1] - u[i0] - v[j]
                if cur < dist[j]:
                    dist[j], pre[j] = cur, j0
                if dist[j] < delta:
                    delta, j1 = dist[j], j
            for j in range(0, m):
                if done[j]:
                    u[p[j]] += delta
                    v[j] -= delta
                else:
                    dist[j] -= delta
            j0 = j1
            if p[j0] == 0: break
        while j0:
            j1 = pre[j0]
            p[j0] = p[j1]
            j0 = j1
    return -v[0], ans
