from collections import *
from itertools import permutations #No repeated elements
import sys, bisect
sys.setrecursionlimit(10**5)
inp = raw_input

def err(s):
    sys.stderr.write('{}\n'.format(s))

def ni():
    return int(inp())

def nl():
    return [int(_) for _ in inp().split()]

# q = deque([0])
# a = q.popleft()
# q.append(0)

# a = [1, 2, 3, 3, 4]
# bisect.bisect(a, 3) == 4
# bisect.bisect_left(a, 3) == 2

