def binarySearchR(coll, val, start, end):
    if start == end:
        return start if coll[start] == val else -1

    mid = (start + end) // 2
    if coll[mid] == val:
        return mid
    elif coll[mid] > val:
        return binarySearchR(coll, val, start, mid)
    else:
        return binarySearchR(coll, val, mid + 1, end)

def binarySearch(coll, val):
    return binarySearchR(coll, val, 0, len(coll))

with open("input.txt") as input:
    lines = input.read().splitlines()
    nums = [int(line) for line in lines]
    nums.sort()
    for i in range(0, len(nums)):
        for j in range(i, len(nums)):
            index = binarySearch(nums, 2020 - nums[i] - nums[j])
            if index != -1:
                x = nums[i]
                y = nums[j]
                z = nums[index]
                print('found', x, y, z, x * y * z)


