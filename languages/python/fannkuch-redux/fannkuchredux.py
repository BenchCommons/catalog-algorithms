# fannkuch-redux, Benchmarks Game definition: prefix reversals over all permutations.
import sys


def fannkuch(n):
    perm1 = list(range(n))
    count = [0] * n
    max_flips = 0
    checksum = 0
    perm_count = 0
    r = n
    while True:
        while r != 1:
            count[r - 1] = r
            r -= 1
        perm = perm1[:]
        flips = 0
        k = perm[0]
        while k:
            perm[:k + 1] = perm[k::-1]
            flips += 1
            k = perm[0]
        max_flips = max(max_flips, flips)
        checksum += flips if perm_count % 2 == 0 else -flips
        while True:
            if r == n:
                return checksum, max_flips
            first = perm1[0]
            perm1[:r] = perm1[1:r + 1]
            perm1[r] = first
            count[r] -= 1
            if count[r] > 0:
                break
            r += 1
        perm_count += 1


n = int(sys.argv[1])
checksum, max_flips = fannkuch(n)
print(checksum)
print("Pfannkuchen(%d) = %d" % (n, max_flips))
