private static class BIT {
  long[] data;
  public BIT(int size) {
    data = new long[size+1];
  }
  public void update(int i, int delta) {
    while(i< data.length) {
      data[i] += delta;
      i += i&-i; // Integer.lowestOneBit(i);
    }
  }
  public long sum(int i) {
    long sum = 0;
    while(i>0) {
      sum += data[i];
      i -= i&-i;
    }
    return sum;
  }
}
