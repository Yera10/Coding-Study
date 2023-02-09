nums = input()

s = 1
for i in range(len(nums)-1):
    if nums[i]!=nums[i+1]:
        s += 1

print(s//2)