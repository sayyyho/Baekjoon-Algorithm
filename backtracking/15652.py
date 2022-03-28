n, m = map(int, input().split())
res = []

def backtracking(max):
    if (len(res) == m):
        print(" ".join(map(str, res)))
        return
    for i in range(1, n+1):
        if (i >= max):
            res.append(i)
            backtracking(i)
            res.pop()

backtracking(1)