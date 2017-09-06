class LazySegmentTree {
  private int n;
  private int[] lo, hi, sum, delta;
  public LazySegmentTree(int n) {
    this.n = n;
    lo = new int[4*n + 1];
    hi = new int[4*n + 1];
    sum = new int[4*n + 1];
    delta = new int[4*n + 1];
    init();
  }
  public int sum(int a, int b) {
    return sum(1, a, b);
  }
  private int sum(int i, int a, int b) {
    if(b < lo[i] || a > hi[i]) return 0;
    if(a <= lo[i] && hi[i] <= b) return sum(i);
    prop(i);
    int l = sum(2*i, a, b);
    int r = sum(2*i+1, a, b);
    update(i);
    return l + r;

  }
  public void inc(int a, int b, int v) {
    inc(1, a, b, v);
  }
  private void inc(int i, int a, int b, int v) {
    if(b < lo[i] || a > hi[i]) return;
    if(a <= lo[i] && hi[i] <= b) {
      delta[i] += v;
      return;
    }
    prop(i);
    inc(2*i, a, b, v);
    inc(2*i+1, a, b, v);
    update(i);
  }

  private void init() {
    init(1, 0, n-1, new int[n]);
  }
  private void init(int i, int a, int b, int[] v) {
    lo[i] = a;
    hi[i] = b;
    if(a == b) {
      sum[i] = v[a];
      return;
    }
    int m = (a+b)/2;
    init(2*i, a, m, v);
    init(2*i+1, m+1, b, v);
    update(i);
  }
  private void update(int i) {
    sum[i] = sum(2*i) + sum(2*i+1);
  }
  private int range(int i) {
    return hi[i] - lo[i] + 1;
  }
  private int sum(int i) {
    return sum[i] + range(i)*delta[i];
  }
  private void prop(int i) {
    delta[2*i] += delta[i];
    delta[2*i+1] += delta[i];
    delta[i] = 0;
  }
}
