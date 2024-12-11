from collections import defaultdict

with open("input", "r") as f:
    stones = list(map(int, f.read().strip().split()))

ds = defaultdict(int)

for i in stones:
    ds[i] += 1

ans1 = 0
ans2 = 0

def af(n):
    global ds
    for _ in range(n):
        d = defaultdict(int)
        for i in ds.keys():
            if i == 0:
                d[1] += ds[i]
            elif len(str(i)) % 2 == 0:
                d[int(str(i)[:len(str(i))//2])] += ds[i]
                d[int(str(i)[len(str(i))//2:])] += ds[i]
            else:
                d[i * 2024] += ds[i]
        ds = d

af(25)

for i in ds.values():
    ans1 += i

af(50)

for i in ds.values():
    ans2 += i

print(ans1)
print(ans2)

