with open("input", "r") as f:
    lns = [i.strip() for i in f.readlines()]

ans1 = 0
ans2 = 0

pieces = lns[0].split(", ")
tomake = lns[2:]

for s in tomake:
    ways = [0 for _ in range(len(s) + 1)]
    ways[0] = 1
    for i in range(len(s)):
        for p in pieces:
            if s[:i + 1].endswith(p):
                ways[i + 1] += ways[i - len(p) + 1]
    if ways[len(s)] >= 1:
        ans1 += 1
    ans2 += ways[len(s)]

print(ans1)
print(ans2)

