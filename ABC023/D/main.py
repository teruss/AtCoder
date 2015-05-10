def dfs(used, res, hs):
    if used == (1 << len(hs)) - 1:
        
        return
    for i in len(hs):
        if used & (1 << i) == 0:
            res = min(res, dfs(used | (1 << i), res, hs))
    return res

def solve(hs):
    used = 0
    return dfs(used, 1000000000 + 1000000000 * 100000, hs)

if __name__ == "__main__":
    N = int(raw_input())
    hs = [(int(h), int(s)) for h, s in [raw_input().split() for _ in range(N)]]
    print solve(hs)
