private static class ST {
  int leftIndex;
  int rightIndex;
  int sum;
  ST leftNode;
  ST rightNode;
}
static ST makeSgmTree(int[] A, int l, int r) {
  if(l == r) {
    ST node = new ST();
    node.leftIndex = l;
    node.rightIndex = r;
    node.sum = A[l];
    return node;
  }
  int mid = (l+r)/2;
  ST leftNode = makeSgmTree(A,l,mid);
  ST rightNode = makeSgmTree(A,mid+1,r);
  ST root = new ST();
  root.leftIndex = leftNode.leftIndex;
  root.rightIndex = rightNode.rightIndex;
  root.sum = leftNode.sum + rightNode.sum;
  root.leftNode = leftNode;
  root.rightNode = rightNode;
  return root;
}
static int getSum(ST root, int l, int r) {
  if(root.leftIndex>=l && root.rightIndex<=r)
    return root.sum;
  if(root.rightIndex<l || root.leftIndex > r) 
    return 0;
  else
    return getSum(root.leftNode,l,r) + getSum(root.rightNode,l,r);
}
static int updateValueAtIndex(ST root, int index, int newValue) {
  int diff = 0;
  if(root.leftIndex==root.rightIndex && index == root.leftIndex) {
    diff = newValue-root.sum;
    root.sum=newValue;
    return diff;
  }
  int mid = (root.leftIndex + root.rightIndex) / 2;
  if (index <= mid) {
    diff= updateValueAtIndex(root.leftNode, index, newValue);
  } else {
    diff= updateValueAtIndex(root.rightNode, index, newValue);
  }
  root.sum+=diff;
  return diff;
}
