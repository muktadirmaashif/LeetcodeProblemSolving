class Solution:
    def arraySign(self, nums: list[int]) -> int:
        product = 1
        for i in nums:
            product *= i
        
        
        return self.signFunc(product)
    
    def signFunc(self, num: int) -> int:
        if num > 0:
            return 1
        elif num < 0:
            return -1
        else:
            return 0
    
    
sol = Solution()

nums = [-1, -2, -3, -4, 3, 2, 1]
print(sol.arraySign(nums))

nums = [1, 5, 0, 2, -3]
print(sol.arraySign(nums))

nums = [-1, 1, -1, 1, -1]
print(sol.arraySign(nums))
