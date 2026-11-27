// spectral-norm, Benchmarks Game definition: ten power iterations on A^T A.
function a(i, j) {
  return 1.0 / (((i + j) * (i + j + 1)) / 2 + i + 1);
}

function times(u, n, transpose) {
  const out = new Array(n);
  for (let i = 0; i < n; i++) {
    let s = 0.0;
    for (let j = 0; j < n; j++) s += (transpose ? a(j, i) : a(i, j)) * u[j];
    out[i] = s;
  }
  return out;
}

const timesAtA = (u, n) => times(times(u, n, false), n, true);

const n = parseInt(process.argv[2], 10);
let u = new Array(n).fill(1.0);
let v = u;
for (let i = 0; i < 10; i++) {
  v = timesAtA(u, n);
  u = timesAtA(v, n);
}
let vbv = 0.0, vv = 0.0;
for (let i = 0; i < n; i++) {
  vbv += u[i] * v[i];
  vv += v[i] * v[i];
}
console.log(Math.sqrt(vbv / vv).toFixed(9));
