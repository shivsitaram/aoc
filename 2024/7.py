with open("input", "r") as f:
    lns = [[int(i.strip().split(":")[0]), list(map(int, i.strip().split(":")[1].split(" ")[1:]))] for i in f.readlines()]

ans1 = 0
ans2 = 0

def works1(nums, v, idx):
    if idx == 0:
        return v == nums[idx]
    return works1(nums, v / nums[idx], idx - 1) or works1(nums, v - nums[idx], idx - 1)

def works2(nums, v, idx):
    if v < 0:
        return False
    if idx == 0:
        return v == nums[idx]
    if (v % nums[idx] == 0 and works2(nums, v // nums[idx], idx - 1)) or works2(nums, v - nums[idx], idx - 1):
        return True
    if str(v).endswith(str(nums[idx])) and v != nums[idx]:
        return works2(nums, int(str(v)[:-len(str(nums[idx]))]), idx - 1)
    return False

for i in lns:
    if works1(i[1], i[0], len(i[1]) - 1):
        ans1 += i[0]
    if works2(i[1], i[0], len(i[1]) - 1):
        ans2 += i[0]

print(ans1)
print(ans2)

