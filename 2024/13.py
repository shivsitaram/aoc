from math import lcm

C = 10000000000000

with open("input", "r") as f:
    lns = [i.strip().split() for i in f.readlines()]

ans1 = 0
ans2 = 0

def ans(ax, ay, bx, by, px, py):
    lc = lcm(ax, ay)
    m1, m2 = lc // ax, lc // ay 
    ax, bx, px = ax * m1, bx * m1, px * m1 
    ay, by, py = ay * m2, by * m2, py * m2
    y = (px - py) / (bx - by)
    x = (px - bx * y) / ax
    if int(x) != x or int(y) != y or x < 0 or y < 0: return 0
    return int(3 * x + y)

for i in range(0, len(lns), 4):
    ax, ay = int(lns[i][2][2:-1]), int(lns[i][3][2:])
    bx, by = int(lns[i + 1][2][2:-1]), int(lns[i + 1][3][2:])
    px, py = int(lns[i + 2][1][2:-1]), int(lns[i + 2][2][2:])
    ans1 += ans(ax, ay, bx, by, px, py)
    ans2 += ans(ax, ay, bx, by, px + C, py + C)

print(ans1)
print(ans2)

