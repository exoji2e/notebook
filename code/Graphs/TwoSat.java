import java.util.*;
public class TwoSat {
    LinkedList<Integer> stack = new LinkedList<>();
    int counter = 0;
    class Node {
        int id;
        public Node(int id){this.id=id;}
        ArrayList<Node> chs = new ArrayList<>();
        ArrayList<Node> back = new ArrayList<>();
        boolean marked = false;
        int component = -1;
        void dfs() {
            marked = true;
            for(Node v: chs)
                if(!v.marked) v.dfs();
            stack.addFirst(id);
        }
        void dfs2() {
            marked = true;
            for(Node v: back)
                if(!v.marked) v.dfs2();
            component = counter;
        }
    }
    // edgs = List of implications: (x1 or not x2) -> {x1^1, x2^1}, {x2, x1}
    boolean TwoSat(int sz, ArrayList<int[]> edgs) {
        Node[] nodes = new Node[2*sz];
        for(int i = 0;i<2*sz; i++) nodes[i] = new Node(i);
        for(int[] e : edgs){
            nodes[e[0]].chs.add(nodes[e[1]]);
            nodes[e[1]].back.add(nodes[e[0]]);
        }
        for(Node u: nodes) if(!u.marked) u.dfs();
        for(Node u: nodes) u.marked = false;
        while(!stack.isEmpty()){
            Node v = nodes[stack.removeFirst()];
            if(!v.marked) {
                counter += 1;
                v.dfs2();
            }
        }
        for(int i = 0; i<sz; i++) {
            if(nodes[2*i].component == nodes[2*i^1].component){
                return false;
            }
        }
        return true;
    }
}
