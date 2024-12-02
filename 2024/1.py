with open("input", "r") as f:
    ar = [i.split() for i in f.readlines()]

a = []
b = []
for i in ar:
    a.append(int(i[0]))
    b.append(int(i[1]))

a.sort()
b.sort()

ans1 = 0
ans2 = 0
for i in range(len(a)):
    ans1 += abs(b[i] - a[i])
    ans2 += a[i] * b.count(a[i])

print(ans1)
print(ans2)

