def check(HS, v):
    N = len(HS)
    D = [0] * N
    for h, s in HS:
        t = (v - h) / s
        if t < 0:
            return False
        if t < N:
            D[t] += 1
    x = 0
    for t in range(N):
        x += D[t]
        if x > t + 1:
            return False
    return True

def solve(HS):
    N = len(HS)
    p = max(HS, key=lambda (h, s): h + s * (N - 1))
    l = 0
    r = p[0] + p[1] * (N - 1) + 1

    while l + 1 < r:
        mid = (l + r) / 2
        if check(HS, mid):
            r = mid
        else:
            l = mid
    return r

if __name__ == "__main__":
    N = input()
    HS = [tuple(map(int, raw_input().split())) for _ in range(N)]
    print solve(HS)
