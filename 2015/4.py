from hashlib import md5

with open("input", "r") as f:
    s = f.read().strip()

def works(n, v):
    return md5((s + str(v)).encode("utf-8")).hexdigest().startswith("0" * n)

ans1 = 1 
while not works(5, ans1):
    ans1 += 1 

ans2 = 1 
while not works(6, ans2):
    ans2 += 1

print(ans1)
print(ans2)

