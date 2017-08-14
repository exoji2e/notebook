static int max_clique(int n, int[][] board) {
  int fst = n/2;
  int snd = n - fst;
  int[] maxc = new int[1<<fst];
  int max = 1;
  for(int i = 0; i<(1<<fst); i++) {
    for(int a = 0; a<fst; a++) {
      if((i&1<<a) != 0) 
        maxc[i] = Math.max(maxc[i], maxc[i^(1<<a)]);
    }
    boolean ok = true;
    for(int a = 0; a<fst; a++) if((i&1<<a) != 0) {
      for(int b = a+1; b<fst; b++) {
          if((i&1<<b) != 0 && board[a][b] == 0) 
              ok = false;
      }
    }
    if(ok) {
      maxc[i] = Integer.bitCount(i);
      max = Math.max(max, maxc[i]);
    }
  }
  for(int i = 0; i<(1<<snd); i++) {
    boolean ok = true;
    for(int a = 0; a<snd; a++) if((i&1<<a) != 0) {
      for(int b = a+1; b<snd; b++) {
        if((i&1<<b) != 0)
          if(board[a+fst][b+fst] == 0) 
            ok = false;
      }
    }
    if(!ok) continue;
    int mask = 0;
    for(int a = 0; a<fst; a++) {
      ok = true;
      for(int b = 0; b<snd; b++) {
        if((i&1<<b) != 0) {
          if(board[a][b+fst] == 0) ok = false;
        }
      }
      if(ok) mask |= (1<<a);
    }
    max = Math.max(Integer.bitCount(i) + maxc[mask], 
            max);
  }
  return max;
}
