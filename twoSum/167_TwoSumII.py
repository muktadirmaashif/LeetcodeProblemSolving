# Leetcode#167 - Two Sum II
# T.C. O(n) S.C. O(1)

class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        left = 0
        right = len(numbers) - 1

        for i in numbers:
            potentialTarget = numbers[left] + numbers[right]
            if potentialTarget < target:
                left += 1
            elif potentialTarget > target:
                right -= 1
        return [left+1, right+1]
