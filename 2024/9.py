with open("input", "r") as f:
    s = f.read().strip()

ans1 = 0
ans2 = 0

s1 = []
idx = 0
for c in s:
    if idx % 2 == 0:
        for i in range(int(c)):
            s1.append(idx // 2)
    else:
        for i in range(int(c)):
            s1.append(-1)
    idx += 1 

s2 = list(s1)
a1 = 0

for i in reversed(range(len(s1))):
    if s1[i] != -1:
        while a1 < i and s1[a1] != -1:
            a1 += 1 
        if a1 < i:
            s1[a1] = s1[i]
            s1[i] = -1

    if i > 0 and s2[i] != -1 and s2[i] != s2[i - 1]:
        l = i
        while l < len(s2) and s2[l] == s2[i]:
            l += 1
        la = -1
        for j in range(i):
            if s2[j] != -1:
                la = j
                continue
            if j - la == l - i:
                for k in range(la + 1, j + 1):
                    s2[k] = s2[i]
                for k in range(i, l):
                    s2[k] = -1
                break

for i in range(len(s1)):
    if s1[i] != -1:
        ans1 += i * s1[i]
    if s2[i] != -1:
        ans2 += i * s2[i]

print(ans1)
print(ans2)

