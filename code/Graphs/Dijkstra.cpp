#include <iostream>
#include <vector>
#include <queue>
using namespace std;

typedef long long ll;
typedef pair<ll,ll> ii;
typedef vector<ll> vi;
typedef vector<ii> vii;

#define rep(i,a,b) for(int i = a; i < b; i++)
#define inf 1e18

vector<vii> edges; //(dest, weight)
vi dist, proc;
ll N; //#nodes

void dijkstra(ll src){ //stores dist from src in dist
  dist.assign(N,inf); dist[src] = 0;
  proc.assign(N, 0);
  priority_queue< pair<ll,ll> > pq;
  pq.push(make_pair(0,src));
  while (!pq.empty()){
    ll val = -pq.top().first, v = pq.top().second; pq.pop();
    if (!proc[v]){
      rep(i, 0, edges[v].size()){
        if (proc[edges[v][i].first]) continue;
        if (dist[edges[v][i].first] > dist[v]+edges[v][i].second){
          dist[edges[v][i].first] = dist[v]+edges[v][i].second;
          pq.push(make_pair(-dist[edges[v][i].first], edges[v][i].first));
        }
      }
    }
    proc[v] = 1;
  }
}
