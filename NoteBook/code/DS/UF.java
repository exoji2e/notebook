private class Node {
  Node parent;
  int h;
  public Node() {
    parent = this;
    height = 0;
  }
  public Node find() {
    if(parent != this) parent = parent.find();
    return parent;
  }
}
static void union(Node x, Node y) {
  Node xR = x.find(), yR = y.find();
  if(xR == yR) return;
  if(xR.h > yR.h) 
    yR.parent = xR;
  else {
    if(yR.h == xR.h) yR.h++;
    xR.parent = yR;
  }
}

