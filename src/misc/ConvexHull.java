import java.util.*;
public class ConvexHull {
  static class Point implements Comparable<Point> {
    static Point xmin;
    int x, y;
    public Point(int x, int y) {
      this.x = x;this.y = y;
    }
    public int compareTo(Point p) {
      int c = cross(this, xmin, p);
      if(c!=0) return c;
      double d = dist(this,xmin) - dist(p,xmin);
      return (int) Math.signum(d);
    }
  }
  static double dist(Point p1, Point p2) {
    return Math.hypot(p1.x - p2.x, p1.y - p2.y);
  }
  static int cross(Point a, Point b, Point c) {
    int dx1 = b.x - a.x;
    int dy1 = b.y - a.y;
    int dx2 = c.x - b.x;
    int dy2 = c.y - b.y;
    return dx1*dy2 - dx2*dy1;
  }
  Point[] convexHull(Point[] S) {
    int N = S.length;
    // find a point on the convex hull.
    Point xmin = S[0];
    int id = 0;
    for(int i = 0; i<N; i++) {
      Point p = S[i];
      if(xmin.x > p.x || 
         xmin.x == p.x && xmin.y > p.y) {
        xmin = p;
        id = i;
      }
    }
    S[id] = S[N-1];
    S[N-1] = xmin;
    Point.xmin = xmin;
    // Sort on angle to xmin.
    Arrays.sort(S, 0, N-1);
    Point[] H = new Point[N+1];
    H[0] = S[N-2];
    H[1] = xmin;
    for(int i = 0; i<N-1; i++)
      H[i+2] = S[i];
    int M = 1;
    // swipe over the points
    for(int i = 2; i<=N; i++) {
      while(cross(H[M-1],H[M],H[i]) <= 0) {
        if(M>1)
          M--;
        else if (i == N)
          break;
        else
          i += 1;
      }
      M+=1;
      Point tmp = H[M];
      H[M] = H[i];
      H[i] = tmp;
    }
    Point[] Hull = new Point[M];
    for(int i = 0; i<M; i++) 
      Hull[i] = H[i];
    return Hull;
  }
}
