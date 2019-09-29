import java.util.*;
import java.io.*;
public class A {
    void solve(BufferedReader in) throws Exception {
    }
    int toInt(String s) {return Integer.parseInt(s);}
    int[] toInts(String s) {
        String[] a = s.split(" ");
        int[] o = new int[a.length];
        for(int i = 0; i<a.length; i++) 
            o[i] = toInt(a[i]);
        return o;
    }
    public static void main(String[] args) 
    throws Exception {
        BufferedReader in = new BufferedReader
            (new InputStreamReader(System.in));
        (new A()).solve(in);
    }
}
