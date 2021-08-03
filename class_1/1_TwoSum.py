# Leetcode#1 - Two Sum
# T.C. O(n) S.C. O(n)

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dict = {}

        for index in range(len((nums))):
            if nums[index] in dict:
                return [dict[nums[index]], index]
            else:
                dict[target - nums[index]] = index
        return []
