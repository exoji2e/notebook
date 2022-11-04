class Treap{
  int sz;
  int v;
  double y;
  Treap L, R;

  static int sz(Treap t) {
    if(t == null) return 0;
    return t.sz;
  }
  static void update(Treap t) {
    if(t == null) return;
    t.sz = sz(t.L) + sz(t.R) + 1;
  }
  static Treap merge(Treap a, Treap b) {
    if (a == null) return b;
    if(b == null) return a;
    if (a.y < b.y) {
      a.R = merge(a.R, b);
      update(a);
      return a;
    } else {
      b.L = merge(a, b.L);
      update(b);
      return b;
    }
  }
  //inserts middle in left half
  static Treap[] split(Treap t, int x) {
    if (t == null) return new Treap[2];
    if (t.v <= x) {
      Treap[] p = split(t.R, x);
      t.R = p[0];
      p[0] = t;
      return p;
    } else {
      Treap[] p = split(t.L, x);
      t.L = p[1];
      p[1] = t;
      return p;
    }
  }
  //use only with split
  static Treap insert(Treap t, int x) {
    Treap m = new Treap();
    m.v = x;
    m.y = Math.random();
    m.sz = 1;
    Treap[] p = splitK(t, x-1);
    return merge(merge(p[0],m), p[1]);
  }


  //inserts middle in left half
  static Treap[] splitK(Treap t, int x) {
    if (t == null) return new Treap[2];
    if (t.sz < x) return new Treap[]{t, null};
    if (sz(t.L) >= x) {
      Treap[] p = splitK(t.L, x);
      t.L = p[1];
      p[1] = t;
      update(p[0]);
      update(p[1]);
      return p;
    } else if (sz(t.L) + 1 == x){
      Treap r = t.R;
      t.R = null;
      Treap[] p = new Treap[]{t, r};
      update(p[0]);
      update(p[1]);
      return p;
    } else {
      Treap[] p = splitK(t.R, x - sz(t.L)-1);
      t.R = p[0];
      p[0] = t;
      update(p[0]);
      update(p[1]);
      return p;
    }
  }
  //use only with splitK
  static Treap insertK(Treap t, int w, int x) {
    Treap m = new Treap();
    m.v = x;
    m.y = Math.random();
    m.sz = 1;
    Treap[] p = splitK(t, w);
    t = merge(p[0], m);
    return merge(t, p[1]);
  }
  //use only with splitK
  static Treap deleteK(Treap t, int w, int x) {
    Treap[] p = splitK(t, w);
    Treap[] q = splitK(p[0], w-1);
    return merge(q[0], p[1]);
  }

  static Treap Left(Treap t) {
    if (t == null) return null;
    if (t.L == null) return t;
    return Left(t.L);
  }
  static Treap Right(Treap t) {
    if (t == null) return null;
    if (t.R == null) return t;
    return Right(t.R);
  }

}
