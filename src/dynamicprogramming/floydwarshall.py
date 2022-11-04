# Computes distance matrix and next matrix given an edgelist
def FloydWarshall(n, edges):
	INF = 10**9
	dist = [[INF]*n for _ in range(n)]
	nxt = [[None]*n for _ in range(n)]
	for e in edges:
		dist[e[0]][e[1]] = e[2]
		nxt[e[0]][e[1]] = e[1]
	for k in range(n):
		for i in range(n):
			for j in range(n):
				if dist[i][j] > dist[i][k] + dist[k][j]:
					dist[i][j] = dist[i][k] + dist[k][j]
					nxt[i][j] = nxt[i][k]
	return dist, nxt

# Computes the path from i to j given a nextmatrix
def path(i, j, nxt):
	if nxt[i][j] == None: return []
	path = [i]
	while i != j:
		i = nxt[i][j]
		path.append(i)
	return path
