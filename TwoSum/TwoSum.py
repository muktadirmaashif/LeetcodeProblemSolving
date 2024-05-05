from rich import print
import rich.traceback
rich.traceback.install()

# [2, 7, 11, 15] => 9
# [3, 2, 4] => 6
# [3, 3] => 6
#
# BRUTE FORCE
# def twoSum(nums, target):
#     """
#     :type nums: List[int]
#     :type target: int
#     :rtype: List[int]
#     """
#     for i in range(len(nums)):
#         for j in range(i, len(nums)):
#             if i == j:
#                 continue
#             if nums[i] + nums[j] == target:
#                 return (i, j)
#
# USING HASH TABLE/DICTIONARY
def twoSum(nums, target):
    num_dict = {}
    length = len(nums)

    for index in range(length): # 0, 1, 2, 3
        comp = target - nums[index]
        if comp in num_dict:
            return [num_dict[comp], index] # return two indices
        else:
            num_dict[nums[index]] = index # add key:value in num_dict
#
print(twoSum([2, 7, 11, 15], 9))
print(twoSum([3, 2, 4], 6))
print(twoSum([3, 3], 6))

