import math

# Distance between two points 
def dist(p, q):
  return math.hypot(p[0]-q[0], p[1] - q[1])

# Converts two points to a line (a, b, c), 
# ax + by + c = 0
# if p == q, a = b = c = 0 
def pts2line(p, q):
  return (-q[1] + p[1], 
      q[0] - p[0], 
      p[0]*q[1] - p[1]*q[0])

# Distance from a point to a line, 
# given that a != 0 or b != 0 
def distl(l, p):
  return (abs(l[0]*p[0] + l[1]*p[1] + l[2])
      /math.hypot(l[0], l[1]))

# intersects two lines.
# if parallell, returnes False.
def inters(l1, l2):
  a1,b1,c1 = l1
  a2,b2,c2 = l2
  cp = a1*b2 - a2*b1 
  if cp != 0:
    return ((b1*c2 - b2*c1)/cp, (a2*c1 - a1*c2)/cp)
  else:
    return False

# projects a point on a line
def project(l, p):
  a, b, c = l
  return ((b*(b*p[0] - a*p[1]) - a*c)/(a*a + b*b), 
      (a*(a*p[1] - b*p[0]) - b*c)/(a*a + b*b))

# Finds the distance between a point, and
# the Segment AB, the Ray AB and the line AB.
# (distSeg, distHalfinf, distLine)
def distSegP(P, Q, R):
  a, b, c = pts2line(P, Q)
  Rpx, Rpy = project((a,b,c), R)
  dp = min(dist(P, R), dist(Q, R))
  dl = distl((a,b,c), R)
  if (inside(Rpx, P[0], Q[0]) and 
          inside(Rpy, P[1], Q[1])):
    return (dl, dl, dl)
  if insideH((Rpx, Rpy), P, Q):
    return (dp, dl, dl)
  return (dp, dp, dl)

# Finds if A <= i <= B.
def inside(i, A, B):
  return (i-A)*(i-B) <= 0

# Finds if a point i on the line AB 
# is on the segment AB.
def insideS(i, A, B):
  return (inside(i[0], A[0], B[0]) 
    and inside(i[1], A[1], B[1]))

# Finds if a point i on the line AB
# is on the ray AB.
def insideH(i, A, B):
  return ((i[0] - A[0])*(A[0] - B[0]) <= 0 
    and (i[1] - A[1])*(A[1] - B[1]) <= 0)

# Finds if segment AB and CD overlabs.
def overlap(A, B, C, D):
    if A[0] == B[0]:
        return __overlap(A[1], B[1], C[1], D[1])
    else:
        return __overlap(A[0], B[0], C[0], D[0])
# Helper functions
def __overlap(x1, x2, x3, x4):
    x1, x2 = (min(x1,x2), max(x1, x2))
    x3, x4 = (min(x3,x4), max(x3, x4))
    return x2 >= x3 and x1 <= x4

# prints a point
def p(P):
    print(str(P[0]) + ' ' + str(P[1]))

# prints common points between
# two segments AB and CD.
def SegSeg(A, B, C, D):
  eqa = A == B
  eqc = C == D
  if eqa and eqc:
    if A == C:
      p(A)
      return True
    return False
  if eqc:
    eqa, A, B, C, D = (eqc, C, D, A, B)
  if eqa:
    l = pts2line(C, D)
    if (l[0]*A[0] + l[1]*A[1] + l[2] == 0 and 
      inside(A[0], C[0], D[0]) and 
      inside(A[1], C[1], D[1])):
      p(A)
      return True
    return False

  A, B = tuple(sorted([A,B]))
  C, D = tuple(sorted([C,D]))
  l1 = pts2line(A, B)
  l2 = pts2line(C, D)
  if l1[0]*l2[1] == l1[1]*l2[0]:
    if l1[0]*l2[2] == l1[2]*l2[0]:
      if overlap(A, B, C, D):
        if B == C:
          p(B)
          return True
        if D == A:
          p(A)
          return True
        s = sorted([A,B,C,D])
        p(s[1])
        p(s[2])
        return True
      else:
        return False
    else:
      return False
  ix, iy = inters(l1, l2)
  if (inside(ix, A[0], B[0]) and 
    inside(iy, A[1], B[1]) and 
    inside(ix, C[0], D[0]) and 
    inside(iy, C[1], D[1])):
    p((ix, iy))
    return True
  return False

# Intersections between circles
def intersections(c1, c2):
  x1, y1, r1 = c1
  x2, y2, r2 = c2
  if x1 == x2 and y1 == y2 and r1 == r2:
    return False
  if r1 > r2:
    x1, y1, r1, x2, y2, r2 = (x2, y2, r2, x1, y1, r1)
  dist2 = (x1 - x2)*(x1-x2) + (y1 - y2)*(y1 - y2)
  rsq = (r1 + r2)*(r1 + r2)
  if dist2 > rsq or dist2 < (r1-r2)*(r1-r2):
    return []
  elif dist2 == rsq:
    cx = x1 + (x2-x1)*r1/(r1+r2)
    cy = y1 + (y2-y1)*r1/(r1+r2)
    return [(cx, cy)]
  elif dist2 == (r1-r2)*(r1-r2):
    cx = x1 - (x2-x1)*r1/(r2-r1)
    cy = y1 - (y2-y1)*r1/(r2-r1)
    return [(cx, cy)]

  d = math.sqrt(dist2)
  f = (r1*r1 - r2*r2 + dist2)/(2*dist2)
  xf = x1 + f*(x2-x1)
  yf = y1 + f*(y2-y1)
  dx = xf-x1
  dy = yf-y1
  h = math.sqrt(r1*r1 - dx*dx - dy*dy)
  norm = abs(math.hypot(dx, dy))
  p1 = (xf + h*(-dy)/norm, yf + h*(dx)/norm)
  p2 = (xf + h*(dy)/norm, yf + h*(-dx)/norm)
  return sorted([p1, p2])

# Finds the bisector through origo
# between two points by normalizing.
def bisector(p1, p2):
  d1 = math.hypot(p1[0], p2[1])
  d2 = math.hypot(p2[0], p2[1])
  return ((p1[0]/d1 + p2[0]/d2),
          (p1[1]/d1 + p2[1]/d2))


