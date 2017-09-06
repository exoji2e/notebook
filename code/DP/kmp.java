//assumes s.length>=w.length
public static boolean kmp(int [] w, int [] s) { 
  int T[] = new int[w.length];
  T[0] = -1; T[1] = 0;
  int m = 0, i = 2;
  while(i<w.length) {
    if(w[i-1] == w[m]) {
      T[i] = ++m;
      i++;
    } else if (m>0) {
      m = T[m];
    } else {
      T[i] = 0;
      i++;
    }
  }

  m = 0; i = 0;
  while(m+i<s.length){
    if(w[i] == s[m+i]) {
      if(i == w.length - 1)
        return true; //m
      i++;
    } else {
      if(T[i] > -1) {
        m = m + i - T[i];
        i = T[i];
      } else {
        i = 0;
        m = m+1;
      }}}
  return false;
}
