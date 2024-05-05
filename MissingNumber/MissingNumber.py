from rich import print
import rich.traceback
rich.traceback.install()

def missingNumber(nums):
    nums.sort()
    for i in range(len(nums)+1):
        if i not in nums:
            return i

list1 = [3, 0, 1]
list2 = [0, 1]
list3 = [9, 6, 4, 2, 3, 5, 7, 0, 1]
print(missingNumber(list1))
print(missingNumber(list2))
print(missingNumber(list3))


