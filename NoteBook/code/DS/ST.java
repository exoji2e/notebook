private static class ST {
  int li, ri;
  int sum; //change to max/min
  ST lN;
  ST rN;
}
static ST makeSgmTree(int[] A, int l, int r) {
  if(l == r) {
    ST node = new ST();
    node.li = l;
    node.ri = r;
    node.sum = A[l]; //max/min
    return node;
  }
  int mid = (l+r)/2;
  ST lN = makeSgmTree(A,l,mid);
  ST rN = makeSgmTree(A,mid+1,r);
  ST root = new ST();
  root.li = lN.li;
  root.ri = rN.ri;
  root.sum = lN.sum + rN.sum; //max/min
  root.lN = lN;
  root.rN = rN;
  return root;
}
static int getSum(ST root, int l, int r) {//max/min
  if(root.li>=l && root.ri<=r)
    return root.sum; //max/min
  if(root.ri<l || root.li > r) 
    return 0; //minInt/maxInt
  else //max/min
    return getSum(root.lN,l,r) + getSum(root.rN,l,r);
}
static int update(ST root, int i, int val) {
  int diff = 0;
  if(root.li==root.ri && i == root.li) {
    diff = val-root.sum; //max/min
    root.sum=val; //max/min
    return diff; //root.max
  }
  int mid = (root.li + root.ri) / 2;
  if (i <= mid) diff = update(root.lN, i, val);
  else diff = update(root.rN, i, val);
  root.sum+=diff; //ask other child
  return diff; //and compute max/min
}
