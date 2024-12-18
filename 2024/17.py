with open("input", "r") as f:
    lns = [i.strip() for i in f.readlines()]

ans1 = 0
ans2 = 0

ao = int(lns[0].split()[-1])
bo = int(lns[1].split()[-1])
co = int(lns[2].split()[-1])

prog = list(map(int, lns[4].split()[1].split(",")))

def ex(a, b, c):
    def comb(v):
        if v <= 3: return v 
        if v == 4: return a
        if v == 5: return b 
        if v == 6: return c 
        return -1
    i = 0
    out = []
    while i < len(prog):
        if prog[i] == 0:
            a >>= comb(prog[i + 1])
        elif prog[i] == 1:
            b = b ^ prog[i + 1]
        elif prog[i] == 2:
            b = comb(prog[i + 1]) % 8 
        elif prog[i] == 3:
            if a != 0:
                i = prog[i + 1]
                i -= 2 
        elif prog[i] == 4:
            b = b ^ c
        elif prog[i] == 5:
            out.append(comb(prog[i + 1]) % 8)
        elif prog[i] == 6:
            b = a >> comb(prog[i + 1])
        else:
            c = a >> comb(prog[i + 1])
        i += 2
    return out

ans1 = ",".join(list(map(str, ex(ao, bo, co))))

here = [0]

for i in reversed(range(len(prog))):
    nhere = []
    for pa in here:
        for j in range(8):
            if ex(pa * 8 + j, bo, co) == prog[i:]:
                nhere.append(pa * 8 + j)
    here = nhere

ans2 = min(here)

print(ans1)
print(ans2)

