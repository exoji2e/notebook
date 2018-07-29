import math

# Distance between two points 
def dist(p, q):
  return math.hypot(p[0]-q[0], p[1] - q[1])

# Square distance between two points
def d2(p, q):
  return (p[0] - q[0])**2 + (p[1] - q[1])**2

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
    return float(b1*c2 - b2*c1)/cp, float(a2*c1 - a1*c2)/cp
  else:
    return False

# projects a point on a line
def project(l, p):
  a, b, c = l
  return ((b*(b*p[0] - a*p[1]) - a*c)/(a*a + b*b), 
    (a*(a*p[1] - b*p[0]) - b*c)/(a*a + b*b))

# Finds if segment AB and CD overlaps.
def overlap(A, B, C, D):
  def __overlap(x1, x2, x3, x4):
    x1, x2 = (min(x1,x2), max(x1, x2))
    x3, x4 = (min(x3,x4), max(x3, x4))
    return x2 >= x3 and x1 <= x4
  return (__overlap(A[0], B[0], C[0], D[0]) 
    and __overlap(A[1], B[1], C[1], D[1]))


# Returns True if P is inside the segment AB
# Assumes that P, A, B are collinear.
def inside(P, A, B):
  return max(d2(P, A), d2(P, B)) <= d2(A, B)

# Returns a list with points:
# 0 if segments AB does not overlap CD
# 1 if segments intersect in one single point
# 2 points describing the segment of overlap
def SegSeg(A, B, C, D):
  eqa = A == B
  eqc = C == D
  if eqa and eqc:
    if A == C:
      return [A]
    return []
  if eqc:
    eqa, A, B, C, D = eqc, C, D, A, B
  if eqa:
    l = pts2line(C, D)
    if l[0]*A[0] + l[1]*A[1] + l[2] == 0 and inside(A, C, D):
      return [A]
    return []

  A, B = sorted([A,B])
  C, D = sorted([C,D])
  l1 = pts2line(A, B)
  l2 = pts2line(C, D)
  if l1[0]*l2[1] == l1[1]*l2[0]:
    if l1[0]*l2[2] == l1[2]*l2[0]:
      if overlap(A, B, C, D):
        if B == C:
          return [B]
        if D == A:
          return [A]
        s = sorted([A,B,C,D])
        return s[1:3]
      else:
        return []
    else:
      return []
  ix, iy = inters(l1, l2)
  P = ix, iy #Beware of percision errors.
  if inside(P, A, B) and inside(P, C, D):
    return [P]
  return []

# Intersections between circles
def intersections(c1, c2):
  if c1[2] > c2[2]:
      c1, c2 = c2, c1
  x1, y1, r1 = c1
  x2, y2, r2 = c2
  if x1 == x2 and y1 == y2 and r1 == r2:
    return False

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

# Distance from P to origo
def norm(P):
  return (P[0]**2 + P[1]**2 + P[2]**2)**(0.5)

# Finds ditance between point p
# and line A + t*u in 3D
def dist3D(A, u, p):
  AP = tuple(A[i] - p[i] for i in range(3))
  cross = tuple(AP[i]*u[(i+1)%3] - AP[(i+1)%3]*u[i] 
    for i in range(3))
  return norm(cross)/norm(u)

