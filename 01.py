def threesum(nums):
    for i in range(len(nums)):
        s = set()
        a = nums[i]
        for j in range(i + 1, len(nums)):
            b = nums[j]
            if nums[j] in s:
                return a * b * (2020 - a - b)
            else:
                s.add(2020 - a - b)
    return -1

nums_ = []
with open('1.txt') as fp:
    nums_ = [int(num) for num in fp]

print(threesum(nums_))