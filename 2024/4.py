with open("input", "r") as f:
    puzzle = [i.strip() for i in f.readlines()]

ans1 = 0
ans2 = 0

def cons1(s):
    global ans1
    if s in ["XMAS", "SAMX"]:
        ans1 += 1

def cons2(v):
    global ans2 
    if v[0] == v[3] or v[1] == v[2]: return 
    if not all(i in "MS" for i in v): return 
    ans2 += 1

for i in range(len(puzzle)):
    for j in range(len(puzzle[0])):
        try:
            cons1(puzzle[i][j:j+4])
        except: pass

        try:
            cons1(puzzle[i][j] + puzzle[i + 1][j] + puzzle[i + 2][j] + puzzle[i + 3][j])
        except: pass

        try:
            cons1(puzzle[i][j] + puzzle[i + 1][j + 1] + puzzle[i + 2][j + 2] + puzzle[i + 3][j + 3])
        except: pass

        try:
            if i - 3 >= 0: cons1(puzzle[i][j] + puzzle[i - 1][j + 1] + puzzle[i - 2][j + 2] + puzzle[i - 3][j + 3])
        except: pass 

        try:
            if puzzle[i][j] == 'A':
                cons2([puzzle[i - 1][j - 1], puzzle[i - 1][j + 1], puzzle[i + 1][j - 1], puzzle[i + 1][j + 1]])
        except: pass

print(ans1)
print(ans2)

