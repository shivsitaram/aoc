with open("input", "r") as f:
    grid = [i.strip() for i in f.readlines()]

ans1 = 0
ans2 = 0

dx = [-1, 0, 1, 0]
dy = [0, -1, 0, 1]

vis = [[False for _ in range(len(grid[0]))] for _ in range(len(grid))]

area = 0
per = 0
per2 = 0

def dfs(a, b):
    global per
    global per2
    global area

    def notin(x, y):
        return (not (0 <= x < len(grid) and 0 <= y < len(grid[0]))) or grid[x][y] != grid[a][b]

    if vis[a][b]: return
    vis[a][b] = True 

    area += 1 
    for i in range(4):
        p = (i % 2) ^ 1
        if notin(a + dx[i], b + dy[i]):
            if notin(a + dx[p], b + dy[p]) or not notin(a + dx[i] + dx[p], b + dy[i] + dy[p]):
                per2 += 1
            per += 1 
        else:
            dfs(a + dx[i], b + dy[i])

for i in range(len(grid)):
    for j in range(len(grid[0])):
        if not vis[i][j]:
            area = 0
            per = 0
            per2 = 0
            dfs(i, j)
            ans1 += area * per
            ans2 += area * per2

print(ans1)
print(ans2)

