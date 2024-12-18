from queue import Queue

with open("input", "r") as f:
    points = [list(map(int, i.split(","))) for i in f.readlines()]

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

MX, CNT = 70, 12

ans1 = 0
ans2 = 0

def w(cnt):
    vis = [[-1 for _ in range(MX + 1)] for _ in range(MX + 1)]
    for i in range(cnt):
        vis[points[i][0]][points[i][1]] = -2 

    q = Queue()
    q.put([0, 0, 0])

    while q.qsize() > 0:
        cur = q.get()
        if not (0 <= cur[1] <= MX and 0 <= cur[2] <= MX): continue 
        if vis[cur[1]][cur[2]] in [-2, 1]: continue 
        vis[cur[1]][cur[2]] = 1 
        if cur[1] == cur[2] == MX:
            return [True, cur[0]]
        for i in range(4):
            q.put([cur[0] + 1, cur[1] + dx[i], cur[2] + dy[i]])
    return [False]

ans1 = w(CNT)[1]
lo, hi = 1, len(points)
while lo < hi:
    mi = (lo + hi) // 2 
    if w(mi)[0]:
        lo = mi + 1 
    else:
        hi = mi

ans2 = ",".join(map(str, points[lo - 1]))

print(ans1)
print(ans2)
