import java.util.*;
class Node {
  int id;
  LinkedList<Node> ch = new LinkedList<>();
  public Node(int id) {
    this.id = id;
  }
}
public class BiGraph {
  private static int INF = Integer.MAX_VALUE;
  LinkedList<Node> L, R;
  int N, M;
  Node[] U;
  int[] Pair, Dist;
  int nild;
  public BiGraph(LinkedList<Node> L, LinkedList<Node> R){
    N = L.size(); M = R.size();
    this.L = L; this.R = R;
    U = new Node[N+M];
    for(Node n: L) U[n.id] = n;
    for(Node n: R) U[n.id] = n;
  }
  private boolean bfs() {
    LinkedList<Node> Q = new LinkedList<>();
    for(Node n: L) 
      if(Pair[n.id] == -1) {
        Dist[n.id] = 0;
        Q.add(n);
      }else 
        Dist[n.id] = INF;

    nild = INF;
    while(!Q.isEmpty()) {
      Node u = Q.removeFirst();
      if(Dist[u.id] < nild) 
        for(Node v: u.ch) if(distp(v) == INF){
          if(Pair[v.id] == -1) 
            nild = Dist[u.id] + 1;
          else {
            Dist[Pair[v.id]] = Dist[u.id] + 1;
            Q.addLast(U[Pair[v.id]]);
          }
        }
    }
    return nild != INF;
  }
  private int distp(Node v) {
    if(Pair[v.id] == -1) return nild;
    return Dist[Pair[v.id]];
  }
  private boolean dfs(Node u) {
    for(Node v: u.ch) if(distp(v) == Dist[u.id] + 1) {
      if(Pair[v.id] == -1 || dfs(U[Pair[v.id]])) {
        Pair[v.id] = u.id;
        Pair[u.id] = v.id;
        return true;
      }
    }
    Dist[u.id] = INF;
    return false;
  }
  public HashMap<Integer, Integer> maxMatch() {
    Pair = new int[M+N];
    Dist = new int[M+N];
    for(int i = 0; i<M+N; i++) {
      Pair[i] = -1;
      Dist[i] = INF;
    }
    HashMap<Integer, Integer> out = new HashMap<>();
    while(bfs()) {
      for(Node n: L) if(Pair[n.id] == -1)
        dfs(n);
    }
    for(Node n: L) if(Pair[n.id] != -1) 
      out.put(n.id, Pair[n.id]);
    return out;
  }
  public HashSet<Integer> minVTC() {
    HashMap<Integer, Integer> Lm = maxMatch();
    HashMap<Integer, Integer> Rm = new HashMap<>();
    for(int x: Lm.keySet()) Rm.put(Lm.get(x), x);
    boolean[] Z = new boolean[M+N];
    LinkedList<Node> bfs = new LinkedList<>();
    for(Node n: L) {
      if(!Lm.containsKey(n.id)) {
        Z[n.id] = true;
        bfs.add(n);
      }
    }
    while(!bfs.isEmpty()) {
      Node x = bfs.removeFirst();
      int nono = -1;
      if(Lm.containsKey(x.id)) 
        nono = Lm.get(x.id);
      for(Node y: x.ch) {
        if(y.id == nono || Z[y.id]) continue;
        Z[y.id] = true;
        if(Rm.containsKey(y.id)){
          int xx = Rm.get(y.id);
          if(!Z[xx]) {
            Z[xx] = true;
            bfs.addLast(U[xx]);
          }
        }
      }
    }
    HashSet<Integer> K = new HashSet<>();
    for(Node n: L) if(!Z[n.id]) K.add(n.id);
    for(Node n: R) if(Z[n.id]) K.add(n.id);
    return K;
  }
}
