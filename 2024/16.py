import heapq

with open("input", "r") as f:
    puzzle = [i.strip() for i in f.readlines()]

ans1 = 0
ans2 = 0

dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]

getto = [[[-1 for _ in range(4)] for _ in range(len(puzzle[0]))] for _ in range(len(puzzle))]

pq = []
for i in range(len(puzzle)):
    for j in range(len(puzzle[0])):
        if puzzle[i][j] == 'S':
            heapq.heappush(pq, (0, i, j, 1))

e1, e2 = 0, 0

while len(pq) > 0:
    el = heapq.heappop(pq)
    if not (0 <= el[1] < len(puzzle) and 0 <= el[2] < len(puzzle[0])): continue
    if puzzle[el[1]][el[2]] == '#': continue
    if getto[el[1]][el[2]][el[3]] != -1: continue 
    if puzzle[el[1]][el[2]] == 'E':
        if ans1 == 0:
            ans1 = el[0]
        e1 = el[1]
        e2 = el[2]
    getto[el[1]][el[2]][el[3]] = el[0]
    heapq.heappush(pq, (el[0] + 1000, el[1], el[2], (el[3] + 1) % 4))
    heapq.heappush(pq, (el[0] + 1000, el[1], el[2], (el[3] - 1) % 4))
    heapq.heappush(pq, (el[0] + 1, el[1] + dx[el[3]], el[2] + dy[el[3]], el[3]))

w = [[False for _ in range(len(puzzle[0]))] for _ in range(len(puzzle))]

for i in range(4):
    heapq.heappush(pq, (-ans1, e1, e2, i))

while len(pq) > 0:
    el = heapq.heappop(pq)
    el = (-el[0], el[1], el[2], el[3])
    if not (0 <= el[1] < len(puzzle) and 0 <= el[2] < len(puzzle[0])): continue
    if getto[el[1]][el[2]][el[3]] == -1: continue 
    if getto[el[1]][el[2]][el[3]] <= el[0]:
        w[el[1]][el[2]] = True 
        heapq.heappush(pq, (-(el[0] - 1000), el[1], el[2], (el[3] + 1) % 4))
        heapq.heappush(pq, (-(el[0] - 1000), el[1], el[2], (el[3] - 1) % 4))
        heapq.heappush(pq, (-(el[0] - 1), el[1] - dx[el[3]], el[2] - dy[el[3]], el[3]))

ans2 = sum(i.count(True) for i in w)

print(ans1)
print(ans2)

