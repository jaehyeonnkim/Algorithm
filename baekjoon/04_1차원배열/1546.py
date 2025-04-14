N = int(input())
nums = list(map(int, input().split()))

max = max(nums)
for idx in range(len(nums)):
    nums[idx] = nums[idx]/max * 100

print(sum(nums)/N)
