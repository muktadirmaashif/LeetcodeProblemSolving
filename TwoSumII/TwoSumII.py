from rich import print
import rich.traceback
rich.traceback.install()
# TWO POINTER - works with sorted array
def twoSum(numbers, target):
    left, right = 0, len(numbers)-1
    for i in range(len(numbers)):
        if numbers[left] + numbers[right] > target:
            right = right - 1
        elif numbers[left] + numbers[right] < target:
            left = left + 1 
        else:
            return [left+1, right+1]

print(twoSum([2, 7, 11, 15], 9))
print(twoSum([2, 3, 4], 6))
print(twoSum([3, 3], 6))
