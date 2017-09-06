import java.util.*;
class Node {
  LinkedList<Edge> edges = new LinkedList<>();
  int id;
  boolean visited = false;
  Edge last = null;
  public Node(int id) {
    this.id = id;
  }
  public void append(Edge e) {
    edges.add(e);
  }
}
class Edge {
  Node source, sink;
  int cap;
  int id;
  Edge redge;
  public Edge(Node u, Node v, int w, int id){
    source = u; sink = v;
    cap = w;
    this.id = id;
  }
}
class FlowNetwork {
  Node[] adj;
  int edgec = 0;
  HashMap<Integer,Integer> flow = new HashMap<>();
  ArrayList<Edge> real = new ArrayList<Edge>();
  public FlowNetwork(int size) {
    adj = new Node[size];
    for(int i = 0; i<size; i++) {
      adj[i] = new Node(i);
    }
  }
  void add_edge(int u, int v, int w, int id){
    Node Nu = adj[u], Nv = adj[v];
    Edge edge = new Edge(Nu, Nv, w, edgec++);
    Edge redge = new Edge(Nv, Nu, 0, edgec++);
    edge.redge = redge;
    redge.redge = edge;
    real.add(edge);
    adj[u].append(edge);
    adj[v].append(redge);
    flow.put(edge.id, 0);
    flow.put(redge.id, 0);
  }

  void reset() {
    for(int i = 0; i<adj.length; i++) {
      adj[i].visited = false; adj[i].last = null;
    }
  }

  LinkedList<Edge> find_path(Node s, Node t, 
          List<Edge> path){
    reset();
    LinkedList<Node> active = new LinkedList<>();
    active.add(s);
    while(!active.isEmpty() && !t.visited) {
      Node now = active.pollFirst();
      for(Edge e: now.edges) {
        int residual = e.cap - flow.get(e.id);
        if(residual>0 && !e.sink.visited) {
          e.sink.visited = true;
          e.sink.last = e;
          active.addLast(e.sink);
        }
      }
    }
    if(t.visited) {
      LinkedList<Edge> res = new LinkedList<>();
      Node curr = t;
      while(curr != s) {
        res.addFirst(curr.last);
        curr = curr.last.sink;
      }
      return res;
    } else return null;
  }

  int max_flow(int s, int t) {
    Node source = adj[s];
    Node sink = adj[t];
    LinkedList<Edge> path = find_path(source, sink, 
            new LinkedList<Edge>());
    while (path != null) {
      int min = Integer.MAX_VALUE;
      for(Edge e : path) {
        min = Math.min(min, e.cap - flow.get(e.id));
      }
      for (Edge e : path) {
        flow.put(e.id, flow.get(e.id) + min);
        Edge r = e.redge;
        flow.put(r.id, flow.get(r.id) - min);
      }
      path = find_path(source, sink, 
              new LinkedList<Edge>());
    }
    int sum = 0;
    for(Edge e: source.edges) {
      sum += flow.get(e.id);
    }
    return sum;
  }

  LinkedList<Edge> min_cut(int s, int t) {
    HashSet<Node> A = new HashSet<>();
    LinkedList<Node> bfs = new LinkedList<>();
    bfs.add(adj[s]);
    A.add(adj[s]);
    while(!bfs.isEmpty()) {
      Node i = bfs.removeFirst();
      for(Edge e: i.edges) {
        int c = e.cap - flow.get(e.id);
        if(c > 0 && !A.contains(e.sink)) {
          bfs.add(e.sink);
          A.add(e.sink);
          if(e.sink.id == t) return null;
        }
      }
    }
    LinkedList<Edge> out = new LinkedList<>();
    for(Node n: A) for(Edge e: n.edges)
        if(!A.contains(e.sink) && e.cap != 0) 
            out.add(e);
    return out;
  }
}
