with open("input", "r") as f:
    grid = [list(i.strip()) for i in f.readlines()]

def out(x, y):
    return not (0 <= x < len(grid) and 0 <= y < len(grid[0]))

ans1 = 0
ans2 = 0

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

do = 0
sx, sy = 0, 0
for i in range(len(grid)):
    for j in range(len(grid[0])):
        if grid[i][j] == '^':
            sx, sy = i, j

def countvis(x, y, d):
    vis = [[False for _ in range(len(grid[0]))] for _ in range(len(grid))]
    vist = [[[False for _ in range(4)] for _ in range(len(grid[0]))] for _ in range(len(grid))]
    loop = False
    while not out(x, y):
        vis[x][y] = True
        if vist[x][y][d]:
            loop = True
            break
        vist[x][y][d] = True
        if out(x + dx[d], y + dy[d]) or grid[x + dx[d]][y + dy[d]] != '#':
            x += dx[d]
            y += dy[d]
        else:
            d = (d + 1) % 4
    return [sum(i.count(True) for i in vis), loop]

ans1 = countvis(sx, sy, do)[0]

for i in range(len(grid)):
    for j in range(len(grid[0])):
        if grid[i][j] != '#':
            grid[i][j] = '#'
            if countvis(sx, sy, do)[1]:
                ans2 += 1 
            grid[i][j] = '.'

print(ans1)
print(ans2)

