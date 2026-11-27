/* spectral-norm, Benchmarks Game definition: ten power iterations on A^T A. */
#include <math.h>
#include <stdio.h>
#include <stdlib.h>

static double a(long i, long j) { return 1.0 / (double)(((i + j) * (i + j + 1)) / 2 + i + 1); }

static void times(double *out, const double *u, long n, int transpose) {
  for (long i = 0; i < n; i++) {
    double s = 0.0;
    for (long j = 0; j < n; j++) s += (transpose ? a(j, i) : a(i, j)) * u[j];
    out[i] = s;
  }
}

static void times_at_a(double *out, const double *u, double *tmp, long n) {
  times(tmp, u, n, 0);
  times(out, tmp, n, 1);
}

int main(int argc, char **argv) {
  long n = argc > 1 ? atol(argv[1]) : 100;
  double *u = malloc(n * sizeof *u), *v = malloc(n * sizeof *v), *tmp = malloc(n * sizeof *tmp);
  for (long i = 0; i < n; i++) u[i] = 1.0;
  for (int i = 0; i < 10; i++) {
    times_at_a(v, u, tmp, n);
    times_at_a(u, v, tmp, n);
  }
  double vbv = 0.0, vv = 0.0;
  for (long i = 0; i < n; i++) {
    vbv += u[i] * v[i];
    vv += v[i] * v[i];
  }
  printf("%.9f\n", sqrt(vbv / vv));
  free(u); free(v); free(tmp);
  return 0;
}
