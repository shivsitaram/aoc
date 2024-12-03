with open("input", "r") as f:
    s = f.read().strip()

ans1 = 0
ans2 = 0
good = True

while len(s) >= 4:
    if s[:4] == "mul(":
        ne = s.find(")")
        if ne != -1:
            nums = s[4:ne].split(",")
            if len(nums) == 2 and all((i.isnumeric() and 1 <= int(i) <= 1000) for i in nums):
                nums = list(map(int, nums))
                ans1 += nums[0] * nums[1]
                if good:
                    ans2 += nums[0] * nums[1]

    if s[:4] == "do()":
        good = True

    if len(s) >= 7 and s[:7] == "don't()":
        good = False
    
    s = s[1:]

print(ans1)
print(ans2)

