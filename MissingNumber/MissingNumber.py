from rich import print
import rich.traceback
rich.traceback.install()


# with sorting, O(nlogn)
def missingNumber(nums):
    nums.sort()
    for i in range(len(nums)+1):
        if i not in nums:
            return i


# without sorting, using sum. O(n)
    rlist = []
    for i in range(len(nums)+1):
        rlist.append(i)
    rsum = numSum = 0
    rsum = sum(i for i in rlist)
    numSum = sum(i for i in nums)
    result = rsum - numSum
    return result


list1 = [3, 0, 1]
list2 = [0, 1]
list3 = [9, 6, 4, 2, 3, 5, 7, 0, 1]
print(missingNumber(list1))
print(missingNumber(list2))
print(missingNumber(list3))
