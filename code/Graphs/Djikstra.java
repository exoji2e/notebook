//Requires java.util.LinkedList and java.util.TreeSet
private static class Node implements Comparable<Node>{
  LinkedList<Edge> edges = new LinkedList<>();
  int w;
  int id;
  public Node(int id) {
    w = Integer.MAX_VALUE;
    this.id = id;
  }
  public int compareTo(Node n) {
    if(w != n.w) return w - n.w;
    return id - n.id;
  }
  //Asumes all nodes have weight MAXINT.
  public int djikstra(Node x) {
    this.w = 0;
    TreeSet<Node> set = new TreeSet<>();
    set.add(this);
    while(!set.isEmpty()) {
      Node curr = set.pollFirst();
      if(x == curr) return x.w;
      for(Edge e: curr.edges) {
        Node other = e.u == curr? e.v : e.u;
        if(other.w > e.cost + curr.w) {
          set.remove(other);
          other.w = e.cost + curr.w;
          set.add(other);
        }
      }
    }
    return -1;
  }
}
private static class Edge {
  Node u,v;
  int cost;
  public Edge(Node u, Node v, int c) {
    this.u = u; this.v = v;
    cost = c;
  }
}
