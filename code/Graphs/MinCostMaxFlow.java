class MinCostMaxFlow {
boolean found[];
int N, dad[];
long cap[][], flow[][], cost[][], dist[], pi[];

static final long INF = Long.MAX_VALUE / 2 - 1;

boolean search(int s, int t) {
Arrays.fill(found, false);
Arrays.fill(dist, INF);
dist[s] = 0;

while (s != N) {
  int best = N;
  found[s] = true;
  for (int k = 0; k < N; k++) {
    if (found[k]) continue;
    if (flow[k][s] != 0) {
      long val = dist[s] + pi[s] - pi[k] - cost[k][s];
      if (dist[k] > val) {
        dist[k] = val;
        dad[k] = s;
      }
    }
    if (flow[s][k] < cap[s][k]) {
      long val = dist[s] + pi[s] - pi[k] + cost[s][k];
      if (dist[k] > val) {
        dist[k] = val;
        dad[k] = s;
      }
    }

    if (dist[k] < dist[best]) best = k;
  }
  s = best;
}
for (int k = 0; k < N; k++)
  pi[k] = Math.min(pi[k] + dist[k], INF);
return found[t];
}

long[] mcmf(long c[][], long d[][], int s, int t) {
cap = c;
cost = d;

N = cap.length;
found = new boolean[N];
flow = new long[N][N];
dist = new long[N+1];
dad = new int[N];
pi = new long[N];

long totflow = 0, totcost = 0;
while (search(s, t)) {
  long amt = INF;
  for (int x = t; x != s; x = dad[x])
    amt = Math.min(amt, flow[x][dad[x]] != 0 ? 
    flow[x][dad[x]] : cap[dad[x]][x] - flow[dad[x]][x]);
  for (int x = t; x != s; x = dad[x]) {
    if (flow[x][dad[x]] != 0) {
      flow[x][dad[x]] -= amt;
      totcost -= amt * cost[x][dad[x]];
    } else {
      flow[dad[x]][x] += amt;
      totcost += amt * cost[dad[x]][x];
    }
  }
  totflow += amt;
}

return new long[]{ totflow, totcost };
}
}
