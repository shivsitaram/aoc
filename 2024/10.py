with open("input", "r") as f:
    grid = [i.strip() for i in f.readlines()]

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

ans1 = 0
ans2 = 0

vis = []

def dfs(a, b, p):
    global ans2
    if not (0 <= a < len(grid) and 0 <= b < len(grid[0])): return
    if int(grid[a][b]) != int(p) + 1: return
    if grid[a][b] == '9': 
        vis[a][b] = True
        ans2 += 1 
    for i in range(4):
        dfs(a + dx[i], b + dy[i], grid[a][b])

for i in range(len(grid)):
    for j in range(len(grid[0])):
        vis = [[False for _ in range(len(grid[0]))] for _ in range(len(grid))]
        dfs(i, j, -1)
        ans1 += sum(i.count(True) for i in vis)

print(ans1)
print(ans2)

