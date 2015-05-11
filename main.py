def solve(R, C, K, rc):
    rows = {}
    columns = {}
    for r, c in rc:
        if not r in rows:
            rows[r] = 0
        rows[r] += 1
        if not c in columns:
            columns[c] = 0
        columns[c] += 1

    numColumnsForCandy = {}
    for v in columns.values():
        if v not in numColumnsForCandy:
            numColumnsForCandy[v] = 0
        numColumnsForCandy[v] += 1
    numColumnsForCandy[0] = C - len(columns)

    res = 0
    for row in rows:
        remain = K - rows[row]
        if remain in numColumnsForCandy:
            res += numColumnsForCandy[remain]

    numRowsWithNoCandy = R - len(rows)
    if K in numColumnsForCandy:
        res += numColumnsForCandy[K] * numRowsWithNoCandy

    for r, c in rc:
        if rows[r] + columns[c] == K:
            res -= 1
        if rows[r] + columns[c] - 1 == K:
            res += 1

    return res

if __name__ == "__main__":
    R, C, K = map(int, raw_input().split())
    candies = [tuple(map(int, raw_input().split())) for _ in range(input())]
    print solve(R, C, K, candies)
