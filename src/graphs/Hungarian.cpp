#include <bits/stdc++.h>
using namespace std;

#define rep(i, a, b) for(int i = a; i < (b); ++i)
#define trav(a, x) for(auto& a : x)
#define sz(x) (int)(x).size()
#define all(x) x.begin(), x.end()
typedef long long ll;
typedef pair<int, int> pii;
typedef vector<int> vi;

typedef vector<ll> vd;
bool zero(ll x) { return x == 0; }
// vector<vd> cost(sz, vd(sz, 0));
// Max Cost found by negating weights.
double MinCostMatching(const vector<vd>& cost) {
	int n = sz(cost), mated = 0;
	vd dist(n), u(n), v(n);
	vi dad(n), seen(n);

	/// construct dual feasible solution
	rep(i,0,n) {
		u[i] = cost[i][0];
		rep(j,1,n) u[i] = min(u[i], cost[i][j]);
	}
	rep(j,0,n) {
		v[j] = cost[0][j] - u[0];
		rep(i,1,n) v[j] = min(v[j], cost[i][j] - u[i]);
	}

	/// find primal solution satisfying complementary slackness
	vi L(n, -1);
	vi R(n, -1);
	rep(i,0,n) rep(j,0,n) {
		if (R[j] != -1) continue;
		if (zero(cost[i][j] - u[i] - v[j])) {
			L[i] = j;
			R[j] = i;
			mated++;
			break;
		}
	}

	for (; mated < n; mated++) { // until solution is feasible
		int s = 0;
		while (L[s] != -1) s++;
		fill(all(dad), -1);
		fill(all(seen), 0);
		rep(k,0,n)
			dist[k] = cost[s][k] - u[s] - v[k];

		int j = 0;
		for (;;) { /// find closest
			j = -1;
			rep(k,0,n){
				if (seen[k]) continue;
				if (j == -1 || dist[k] < dist[j]) j = k;
			}
			seen[j] = 1;
			int i = R[j];
			if (i == -1) break;
			rep(k,0,n) { /// relax neighbors
				if (seen[k]) continue;
				auto new_dist = dist[j] + cost[i][k] - u[i] - v[k];
				if (dist[k] > new_dist) {
					dist[k] = new_dist;
					dad[k] = j;
				}
			}
		}

		/// update dual variables
		rep(k,0,n) {
			if (k == j || !seen[k]) continue;
			auto w = dist[k] - dist[j];
			v[k] += w, u[R[k]] -= w;
		}
		u[s] += dist[j];

		/// augment along path
		while (dad[j] >= 0) {
			int d = dad[j];
			R[j] = R[d];
			L[R[j]] = j;
			j = d;
		}
		R[j] = s;
		L[s] = j;
	}
	auto value = vd(1)[0];
	rep(i,0,n) value += cost[i][L[i]];
	return value;
}
