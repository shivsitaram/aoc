with open("input", "r") as f:
    lines = [list(map(int, i.split())) for i in f.readlines()]

def good(v):
    if v == sorted(v) or v == list(reversed(sorted(v))):
        for j in range(len(v) - 1):
            if not 1 <= abs(v[j + 1] - v[j]) <= 3:
                return False
        return True
    return False

ans1 = 0
ans2 = 0
for i in lines:
    if good(i):
        ans1 += 1 
        ans2 += 1
        continue

    ow = False
    for j in range(len(i)):
        ni = list(i)
        ni.pop(j)
        if good(ni):
            ow = True

    if ow:
        ans2 += 1

print(ans1)
print(ans2)

