// C++ implementation of Dinic's Algorithm
// O(V*V*E) for generall flow-graphs. (But with a good constant)
// O(E*sqrt(V)) for bipartite matching graphs.
// O(E*min(V**(2/3),E**(1/3))) For unit-capacity graphs
#include<bits/stdc++.h>
using namespace std;
typedef long long ll;
struct Edge{
  ll v ;//to vertex
  ll flow ;
  ll C;//capacity
  ll rev;//reverse edge index
};
// Residual Graph
class Graph
{
public:
  ll V; // number of vertex
  vector<ll> level; // stores level of a node
  vector<vector<Edge>> adj; //can also be array of vector with global size
  Graph(ll V){
    adj.assign(V,vector<Edge>());
    this->V = V;
    level.assign(V,0);
  }

  void addEdge(ll u, ll v, ll C){
    Edge a{v, 0, C, (int)adj[v].size()};// Forward edge
    Edge b{u, 0, 0, (int)adj[u].size()};// Back edge
    adj[u].push_back(a);
    adj[v].push_back(b); // reverse edge
  }

  bool BFS(ll s, ll t){
    for (ll i = 0 ; i < V ; i++)
        level[i] = -1;
    level[s] = 0;  // Level of source vertex
    list< ll > q;
    q.push_back(s);
    vector<Edge>::iterator i ;
    while (!q.empty()){
      ll u = q.front();
      q.pop_front();
      for (i = adj[u].begin(); i != adj[u].end(); i++){
        Edge &e = *i;
        if (level[e.v] < 0  && e.flow < e.C){
          level[e.v] = level[u] + 1;
          q.push_back(e.v);
        }
      }
    }
    return level[t] < 0 ? false : true; //can/cannot reach target
  }

  ll sendFlow(ll u, ll flow, ll t, vector<ll> &start){
    // Sink reached
    if (u == t)
        return flow;
    // Traverse all adjacent edges one -by - one.
    for (  ; start[u] < (int)adj[u].size(); start[u]++){
      Edge &e = adj[u][start[u]];
      if (level[e.v] == level[u]+1 && e.flow < e.C){
        // find minimum flow from u to t
        ll curr_flow = min(flow, e.C - e.flow);
        ll temp_flow = sendFlow(e.v, curr_flow, t, start);
        // flow is greater than zero
        if (temp_flow > 0){
          e.flow += temp_flow;//add flow
          adj[e.v][e.rev].flow -= temp_flow;//sub from reverse edge
          return temp_flow;
        }
      }
    }
    return 0;
  }
  ll DinicMaxflow(ll s, ll t){
    // Corner case
    if (s == t) return -1;
    ll total = 0;  // Initialize result
    while (BFS(s, t) == true){//while path from s to t
      // store how many edges are visited
      // from V { 0 to V }
      vector <ll> start;
      start.assign(V,0);
      // while flow is not zero in graph from S to D
      while (ll flow = sendFlow(s, 999999999, t, start))
        total += flow;// Add path flow to overall flow
    }
    return total;
  }
};
