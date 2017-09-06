import java.util.StringTokenizer;
import java.io.*;
class Sc {
  public Sc(InputStream i) {
    r = new BufferedReader(new InputStreamReader(i));
  }
  public boolean hasM() {
    return peekToken() != null;
  }
  public int nI() {
    return Integer.parseInt(nextToken());
  }
  public double nD() { 
    return Double.parseDouble(nextToken());
  }
  public long nL() {
    return Long.parseLong(nextToken());
  }
  public String n() {
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
}
