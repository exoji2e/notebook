//Computes A^-1 * b
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
      for (int k = i+1; k < N; k++)
        A[j][k] -= A[i][k] * m;
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
