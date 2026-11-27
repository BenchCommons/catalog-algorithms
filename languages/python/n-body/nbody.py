# n-body, Benchmarks Game definition (5 Jovian bodies), plain CPython.
import sys

PI = 3.14159265358979323
SOLAR_MASS = 4 * PI * PI
DAYS = 365.24

BODIES = {
    'sun': ([0.0, 0.0, 0.0], [0.0, 0.0, 0.0], SOLAR_MASS),
    'jupiter': ([4.84143144246472090e+00, -1.16032004402742839e+00, -1.03622044471123109e-01],
                [1.66007664274403694e-03 * DAYS, 7.69901118419740425e-03 * DAYS,
                 -6.90460016972063023e-05 * DAYS], 9.54791938424326609e-04 * SOLAR_MASS),
    'saturn': ([8.34336671824457987e+00, 4.12479856412430479e+00, -4.03523417114321381e-01],
               [-2.76742510726862411e-03 * DAYS, 4.99852801234917238e-03 * DAYS,
                2.30417297573763929e-05 * DAYS], 2.85885980666130812e-04 * SOLAR_MASS),
    'uranus': ([1.28943695621391310e+01, -1.51111514016986312e+01, -2.23307578892655734e-01],
               [2.96460137564761618e-03 * DAYS, 2.37847173959480950e-03 * DAYS,
                -2.96589568540237556e-05 * DAYS], 4.36624404335156298e-05 * SOLAR_MASS),
    'neptune': ([1.53796971148509165e+01, -2.59193146099879641e+01, 1.79258772950371181e-01],
                [2.68067772490389322e-03 * DAYS, 1.62824170038242295e-03 * DAYS,
                 -9.51592254519715870e-05 * DAYS], 5.15138902046611451e-05 * SOLAR_MASS),
}


def offset_momentum(bodies):
    p = [0.0, 0.0, 0.0]
    for r, v, m in bodies:
        for i in range(3):
            p[i] -= v[i] * m
    bodies[0][1][:] = [c / SOLAR_MASS for c in p]


def energy(bodies):
    e = 0.0
    for i, (r1, v1, m1) in enumerate(bodies):
        e += 0.5 * m1 * (v1[0] ** 2 + v1[1] ** 2 + v1[2] ** 2)
        for r2, v2, m2 in bodies[i + 1:]:
            d = [r1[k] - r2[k] for k in range(3)]
            e -= m1 * m2 / (d[0] ** 2 + d[1] ** 2 + d[2] ** 2) ** 0.5
    return e


def advance(bodies, dt, steps):
    pairs = [(a, b) for i, a in enumerate(bodies) for b in bodies[i + 1:]]
    for _ in range(steps):
        for (r1, v1, m1), (r2, v2, m2) in pairs:
            dx, dy, dz = r1[0] - r2[0], r1[1] - r2[1], r1[2] - r2[2]
            mag = dt * ((dx * dx + dy * dy + dz * dz) ** -1.5)
            b1m, b2m = m1 * mag, m2 * mag
            v1[0] -= dx * b2m
            v1[1] -= dy * b2m
            v1[2] -= dz * b2m
            v2[0] += dx * b1m
            v2[1] += dy * b1m
            v2[2] += dz * b1m
        for r, v, m in bodies:
            r[0] += dt * v[0]
            r[1] += dt * v[1]
            r[2] += dt * v[2]


def main(n):
    bodies = [[list(r), list(v), m] for r, v, m in BODIES.values()]
    offset_momentum(bodies)
    print('%.9f' % energy(bodies))
    advance(bodies, 0.01, n)
    print('%.9f' % energy(bodies))


main(int(sys.argv[1]))
