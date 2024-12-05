with open("input", "r") as f:
    lns = [i.strip() for i in f.readlines()]

ans1 = 0
ans2 = 0

currules = True
rules = [[] for _ in range(100)]
for i in lns:
    if i == "":
        currules = False
        continue 

    if currules:
        i = list(map(int, i.split("|")))
        rules[i[0]].append(i[1])
    else:
        nums = list(map(int, i.split(",")))
        works = True
        for j in range(len(nums)):
            for k in range(j + 1, len(nums)):
                if nums[j] in rules[nums[k]]:
                    works = False
                    nums[j], nums[k] = nums[k], nums[j]

        if works:
            ans1 += nums[len(nums) // 2] 
        else:
            ans2 += nums[len(nums) // 2]

print(ans1)
print(ans2)

