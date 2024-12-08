with open("input", "r") as f:
    lns = [i.strip() for i in f.readlines()]

ans1 = 0
ans2 = 0

works1 = [[False for _ in range(len(lns[0]))] for _ in range(len(lns))]
works2 = [[False for _ in range(len(lns[0]))] for _ in range(len(lns))]

for a1 in range(len(lns)):
    for b1 in range(len(lns[0])):
        for a2 in range(len(lns)):
            for b2 in range(len(lns[0])):
                if lns[a1][b1] == lns[a2][b2] and lns[a1][b1] != '.' and (a1, b1) != (a2, b2):
                    works2[a1][b1] = works2[a2][b2] = True
                    a = a1 + a1 - a2 
                    b = b1 + b1 - b2 
                    done = False
                    while 0 <= a < len(lns) and 0 <= b < len(lns[0]):
                        if not done: works1[a][b] = True
                        works2[a][b] = True
                        done = True
                        a += a1 - a2
                        b += b1 - b2

ans1 = sum(i.count(True) for i in works1)
ans2 = sum(i.count(True) for i in works2)

print(ans1)
print(ans2)

