//TODO: split into smaller files that TeX can read and generate a good pdf from.
//Segmentträd
private static class STNode {
    int leftIndex;
    int rightIndex;
    int sum;
    STNode leftNode;
    STNode rightNode;
}
static STNode makeSgmTree(int[] A, int l, int r) {
    if(l == r) {
        STNode node = new STNode();
        node.leftIndex = l;
        node.rightIndex = r;
        node.sum = A[l];
        return node;
    }
    int mid = (l+r)/2;
    STNode leftNode = makeSgmTree(A,l,mid);
    STNode rightNode = makeSgmTree(A,mid+1,r);
    STNode root = new STNode();
    root.leftIndex = leftNode.leftIndex;
    root.rightIndex = rightNode.rightIndex;
    root.sum = leftNode.sum + rightNode.sum;
    root.leftNode = leftNode;
    root.rightNode = rightNode;
    return root;
}
static int getSum(STNode root, int l, int r) {
    if(root.leftIndex>=l && root.rightIndex<=r)
        return root.sum;
    if(root.rightIndex<l || root.leftIndex > r) 
        return 0;
    else
        return getSum(root.leftNode,l,r) + getSum(root.rightNode,l,r);
}
static int updateValueAtIndex(STNode root, int index, int newValue) {
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




int[] primes = {10007, 20011, 40009, 80021, 160001, 320009, 640007, 1280023, 2560021, 5120029, 10240033, 40000003};
Arrays.sort(ints);
Comparable.sort(Collection<E> ints, Comparator<E> intcomp);


//Binary search, a måste vara sorterad, minst först
public static int indexOf(int[] a, int key) {
    int lo = 0;
    int hi = a.length - 1;
    while (lo <= hi) {
        // Key is in a[lo..hi] or not present.
        int mid = lo + (hi - lo) / 2;
        if (key < a[mid]) hi = mid - 1;
        else if (key > a[mid]) lo = mid + 1;
        else return mid;
    }
    return -1;
}


//LIS - Longest increasing subsequence O(nlogn)
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







//KMP, O(|w| + |s|) to find if w is a subarray to s
//antag att s.length>w.length
public static boolean kmp(int [] w, int [] s) { 
        int T[] = new int[w.length];
        T[0] = -1;
        T[1] = 0;
        int m = 0;
        int i = 2;
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
        
        m = 0;
        i = 0;
        while(m+i<s.length){
            if(w[i] == s[m+i]) {
                if(i == w.length - 1)
                    return true;
                i++;
            } else {
                if(T[i] > -1) {
                    m = m + i - T[i];
                    i = T[i];
                } else {
                    i = 0;
                    m = m+1;
                }
            }
        }
        return false;
    }

















//Closets pair of points:

public static double divc(Point[] xp, Point[] yp, int size) {
    if(size == 2) {
        return xp[0].dist(xp[1]);
    }
    if(size == 3) {
        return Math.min(Math.min(xp[0].dist(xp[1]),xp[0].dist(xp[2])),xp[1].dist(xp[2]));
    }
    int mid = (size+1)/2;
    Point splitp = xp[mid];
    Point[] xplo = new Point[mid];
    Point[] xphi = new Point[size-mid];
    Point[] yplo = new Point[mid];
    Point[] yphi = new Point[size-mid];
    int cxlo = 0;
    int cxhi = 0;
    int cylo = 0;
    int cyhi = 0;
    
    for(int i = 0; i<size; i++) {
        if(i < mid) xplo[cxlo++] = xp[i];
        else xphi[cxhi++] = xp[i];
        
        if(yp[i].compareTo(splitp) < 0) yplo[cylo++] = yp[i];
        else yphi[cyhi++] = yp[i];
    }
    
    double min = Math.min(divc(xplo,yplo,mid),divc(xphi,yphi,size-mid));
    
    Point[] strip = new Point[size];
    int count = 0;
    for(int i = 0; i<size; i++) {
        if(Math.abs(yp[i].x - splitp.x) < min)
            strip[count++] = yp[i];
    }
    for(int i = 0; i<count-1; i++) {
        for(int j = i+1; j<i+8 && j<count; j++) {
            double dist = strip[i].dist(strip[j]);
            if(dist<min) {
                min = dist;
            }
        }
    }
    return min;
}






// Convex hull
public Point[] convexHull(Point[] S) {
    Arrays.sort(S); //Sort on angle form some point in the convex hull
    int i = 0;
    Point[] P = new Point[N]; //convex hull
    Point p = S[0];
    boolean passedLast = false;
    int w = i;
    do {
        P[i] = p;
        Point e;
        if(!passedLast) {
            e = S[w+1];
            w = w+1;
            for(int j = w+2; j<N; j++) {
                int c = cross(p,e,S[j]); //z-crossproduct between  
                if(e.equals(p) || c>0 || (c == 0 && dist(p,S[j]) > dist(p,e))) {
                    e = S[j];
                    w= j;
                }
            }
        }else { 
            e = S[w-1];
            w = w-1;
            for(int j = w-2; j>=0; j--) {
                int c = cross(p,e,S[j]);
                if(e.equals(p) || c>0 || (c == 0 && dist(p,S[j]) > dist(p,e))) {
                    e = S[j];
                    w = j;
                }
            }
        }
        i++;
        p = e;
        if(e.equals(S[N-1])) {
            passedLast = true;
        }
    } while(p != P[0]);
    return P;
}
//Z-part of CrossProduct => angle between ab and bc
public static int cross(Point a, Point b, Point c) {
    int dx1 = b.x - a.x;
    int dy1 = b.y - a.y;
    int dx2 = c.x - b.x;
    int dy2 = c.y - b.y;
    return dx1*dy2 - dx2*dy1;
}







// Picks Theorem:
// A = i + b/2 - 1 för godtycklig polygon med heltalskoordinater, 
// i = inneslutna heltalspunkter, b = punkter på kanten.

//Compute A^-1 * b
public static double[] solve(double[][] A, double[] b) {
	int N = b.length;
	// Gaussian elimination with partial pivoting
	for (int i = 0; i < N; i++) {

	    // find pivot row and swap
	    int max = i;
	    for (int j = i + 1; j < N; j++)
	        if (Math.abs(A[j][i]) > Math.abs(A[max][i]))
	            max = j;
	    double[] tmp = A[i];
	    A[i] = A[max];
	    A[max] = tmp;
	    double tmp2 = b[i];
	    b[i] = b[max];
	    b[max] = tmp2;

	    // A doesn't have full rank
	    if (Math.abs(A[i][i])<0.00001) return null;

	    // pivot within b
	    for (int j = i + 1; j < N; j++)
	        b[j] -= b[i] * A[j][i] / A[i][i];

	    // pivot within A
	    for (int j = i + 1; j < N; j++) {
	        double m = A[j][i] / A[i][i];
	        for (int k = i+1; k < N; k++) {
	            A[j][k] -= A[i][k] * m;
	        }
	        A[j][i] = 0.0;
		}
	}

	// back substitution
	double[] x = new double[N];
	for (int j = N - 1; j >= 0; j--) {
	    double t = 0.0;
	    for (int k = j + 1; k < N; k++)
	        t += A[j][k] * x[k];
	    x[j] = (b[j] - t) / A[j][j];
	}
	return x;
}



//Network Flow
private static class Node {
    LinkedList<Edge> edges = new LinkedList<>();
    int id;
    boolean visited = false;
    Edge last = null;
    public Node(int id) {
        this.id = id;
    }
    public void append(Edge e) {
        edges.add(e);
    }
}
private static class Edge {
    Node source, sink;
    int capacity;
    int id;
    Edge redge;
    public Edge(Node u, Node v, int w, int id){
        source = u;
        sink = v;
        capacity = w;
        this.id = id;
    }
}
private static class FlowNetwork {
    Node[] adj;
    int edgec = 0;
    HashMap<Integer,Integer> flow = new HashMap<>();
    ArrayList<Edge> real = new ArrayList<Edge>();
    public FlowNetwork(int size) {
        adj = new Node[size];
        for(int i = 0; i<size; i++) {
            adj[i] = new Node(i);
        }
    }
    public void add_edge(int u, int v, int w, boolean addreal){
        Node Nu = adj[u];
        Node Nv = adj[v];
        Edge edge = new Edge(Nu,Nv,w,edgec++);
        Edge redge = new Edge(Nv,Nu,0,edgec++);
        edge.redge = redge;
        redge.redge = edge;
        if(addreal) real.add(edge);
        adj[u].append(edge);
        adj[v].append(redge);
        flow.put(edge.id,0);
        flow.put(redge.id,0);
    }
    public void reset() {
        for(int i = 0; i<adj.length; i++) {
            adj[i].visited = false; adj[i].last = null;
        }
    }
    public LinkedList<Edge> find_path(Node source, Node sink, LinkedList<Edge> path){
        reset();
        LinkedList<Node> active = new LinkedList<>();
        active.add(source);
        while(!active.isEmpty() && !sink.visited) {
            Node now = active.pollFirst();
            for(Edge e: now.edges) {
                int residual = e.capacity - flow.get(e.id);
                if(residual>0 && !e.sink.visited) {
                    e.sink.visited = true;
                    e.sink.last = e;
                    active.addLast(e.sink);
                }
            }
        }
        if(sink.visited) {
            LinkedList<Edge> res = new LinkedList<>();
            Node curr = sink;
            while(curr!= source) {
                res.addFirst(curr.last);
                curr = curr.last.source;
            }
            return res;
        } else {
            return null;
        }
    }

    public int max_flow(int s, int t) {
        Node source = adj[s];
        Node sink = adj[t];
        LinkedList<Edge> path = find_path(source, sink, new LinkedList<Edge>());
        while (path != null) {
            int min = Integer.MAX_VALUE;
            for(Edge e : path) {
                min = Math.min(min, e.capacity - flow.get(e.id));
            }
            for (Edge e : path) {
                flow.put(e.id, flow.get(e.id) + min);
                Edge r = e.redge;
                flow.put(r.id, flow.get(r.id) - min);
            }
            path = find_path(source, sink, new LinkedList<Edge>());
        }
        int sum = 0;
        for(Edge e: source.edges) {
            sum += flow.get(e.id);
        }
        return sum;
    }
}


public static class XComp implements Comparator<X> {
    public XComp() {
            
    }
    public int compare(X x1, X x2) {
        return x1.compareTo(x2);
    }
}

class X implements Comparable<X> {
    public int compareTo (X x1 ) {
        if(this.tosort!=x1.tosort) return this.tosort - x1.tosort;
    }
}

//Centroid Decomposition:

// Given a tree T, we can build a centroid tree using this approach –

// 1. Find the centroid C of T and make it the root of the centroid tree that we are building.

// 2. Recursively find the centroids of the connected components(think of them as new trees) and add them to the centroid tree.

// 3. As we are limiting the component size as half of the total nodes, its easy to see that the centroid tree will have depth O(log n). Finding the centroid takes at most O(n) time and hence, this tree can be constructed in O(nlogn) time.

// Step 0 : Root the tree arbitrarily.

// Step 1 : Calculate the size of each subtree(excluding the vertex rooted at it).
public void dfs(int current, int parent) {
        size[current] = 0;
        for(int i=0;i<adjacency_list[current].size();i++) {
                int next = adjacency_list[current][i];
                if(next == parent or deleted[next])continue;
                dfs(next, current);
                size[current] += size[next] + 1;
        }
        return ;
}
// Step 2 : Finding the center of the tree.
int findcenter(int current, int parent, int total){  
    for(int i=0;i<(int)adjacency_list[current].size();i++) {
        int next = adjacency_list[current][i];      
        if(next == parent or deleted[next])continue;
        if(total/2 < size[current] + 1)
            return findcenter(next, current, total);
    } 
    return current;
}