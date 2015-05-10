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

    res = 0
    for row in rows:
        for column in columns:
            if rows[row] + columns[column] - (1 if (row, column) in rc else 0) == K:
                res += 1

    for row in rows:
        if rows[row] == K:
            res += C - len(columns)

    for column in columns:
        if columns[column] == K:
            res += R - len(rows)

    return res

if __name__ == "__main__":
    R, C, K = [int(x) for x in raw_input().split()]
    N = int(raw_input())
    rc = [(int(r), int(c)) for r, c in [raw_input().split() for _ in range(N)]]
    print solve(R, C, K, rc)
