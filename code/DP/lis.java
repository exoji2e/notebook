public static int lis(int[] X) { 
  int n = X.length;
  int P[] = new int[n];
  int M[] = new int[n+1];
  int L = 0;
  for(int i = 0; i<n; i++) {
    int lo = 1;
    int hi = L;
    while(lo<=hi) {
      int mid = lo + (hi - lo + 1)/2;
      if(X[M[mid]]<X[i])
        lo = mid+1;
      else
        hi = mid-1;
    }
    int newL = lo;
    P[i] = M[newL-1];
    M[newL] = i;
    if (newL > L)
      L = newL;
    
  }
  int[] S = new int[L];
  int k = M[L];
  for (int i = L-1; i>=0; i--) {
    S[i] = k; //or X[k]
    k = P[k];
  }
  return L; // or S
}
