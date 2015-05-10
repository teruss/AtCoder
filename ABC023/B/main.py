def solve(S):
    N = len(S)
    if N % 2 == 0:
        return -1
    if N == 1:
        if S == "b":
            return 0
        return -1
    if N % 3 == 0:
        if S == "abc" * (N / 3):
            return N / 2
        return -1
    if N % 3 == 1:
        if S == "bc" + "abc" * ((N - 4) / 3) + "ab":
            return N / 2
        return -1
    if N % 3 == 2:
        if S == "c" + "abc" * (N / 3) + "a":
            return N / 2
        return -1

if __name__ == "__main__":
    N = raw_input()
    S = raw_input()
    print solve(S)
