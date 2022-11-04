import java.util.*;
import java.io.*;
public class A {
    void solve(Kattio io) {
        
    }
    void run() {
        Kattio io = new Kattio(System.in, System.out);
        solve(io);
        io.flush();
    }
    public static void main(String[] args) {
        (new A()).run();
    }
    class Kattio extends PrintWriter {
        public Kattio(InputStream i) {
            super(new BufferedOutputStream(System.out));
            r = new BufferedReader(new InputStreamReader(i));
        }
        public Kattio(InputStream i, OutputStream o) {
            super(new BufferedOutputStream(o));
            r = new BufferedReader(new InputStreamReader(i));
        }

        public boolean hasMoreTokens() {
            return peekToken() != null;
        }

        public int getInt() {
            return Integer.parseInt(nextToken());
        }

        public double getDouble() { 
            return Double.parseDouble(nextToken());
        }

        public long getLong() {
            return Long.parseLong(nextToken());
        }

        public String getWord() {
            return nextToken();
        }

        private BufferedReader r;
        private String line;
        private StringTokenizer st;
        private String token;

        private String peekToken() {
            if (token == null) 
                try {
                    while (st == null || !st.hasMoreTokens()) {
                        line = r.readLine();
                        if (line == null) return null;
                        st = new StringTokenizer(line);
                    }
                    token = st.nextToken();
                } catch (IOException e) { }
            return token;
        }

        private String nextToken() {
            String ans = peekToken();
            token = null;
            return ans;
        }
        private String joinRemainder() {
            ArrayList<String> tokens = new ArrayList<>();
            while (st.hasMoreTokens()) {
                tokens.add(st.nextToken());
            }
            return String.join(" ", tokens);
        }
        public String remainingLine() {
            if(st != null && st.hasMoreTokens()) {
                return joinRemainder();
            }
            return nextLine();
        }
        public String nextLine() {
            try {
                return r.readLine();
            } catch(IOException e) {
                return null;
            }
        }
    }
}
