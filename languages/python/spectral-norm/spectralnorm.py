# spectral-norm, Benchmarks Game definition: ten power iterations on A^T A.
import sys
from math import sqrt


def a(i, j):
    return 1.0 / ((i + j) * (i + j + 1) // 2 + i + 1)


def times(u, n, transpose):
    out = []
    for i in range(n):
        s = 0.0
        for j in range(n):
            s += (a(j, i) if transpose else a(i, j)) * u[j]
        out.append(s)
    return out


def times_at_a(u, n):
    return times(times(u, n, False), n, True)


n = int(sys.argv[1])
u = [1.0] * n
v = u
for _ in range(10):
    v = times_at_a(u, n)
    u = times_at_a(v, n)
vbv = vv = 0.0
for i in range(n):
    vbv += u[i] * v[i]
    vv += v[i] * v[i]
print("%.9f" % sqrt(vbv / vv))
