def moveZeroes (nums: list[int]) -> None:
    ## Using list comprehension, T.C O(N), S.C. = O(1), 
    ## Doens't change nums in-place, so if return type None, won't be accesptes

    # count = sum (x== 0 for x in nums) 
    # nums = [x for x in nums if x != 0]           
    #
    # for i in range(count):
    #     nums.append(0)
    # return nums
    #

    ## Modified version of anove approach, just changed in-place, same complexities. 
    # i = 0
    # for x in nums:
    #     print("x = ", x)
    #     if x != 0:
    #         print("Inside if, x = ", x)
    #         nums[i] = x
    #         i += 1
    #         print("inside if, i = ", i)
    #         print("nums = ", nums)
    #
    # for j in range(i, len(nums)):
    #     nums[j] = 0
    # print("final nums = ", nums)

    ## Two Pointer
    non_zero =0 
    for current in range(len(nums)):

        # print(f"current = {current}, non_zero = {non_zero}")
        if nums[current] != 0:
            # print("inside if: ")
            # print(f"current = {current}, currentValue = {nums[current]}, non_zero = {non_zero}")
            nums[current] , nums[non_zero] = nums[non_zero],  nums[current]
            non_zero += 1
        print(nums)

n = [0, 1, 0 , 3, 12]
res = moveZeroes(n)
print(res)

# n = [0, 1, 0 , 3, 2]
# res = moveZeroes(n)
# print(res)
#
# n = [0]
# res = moveZeroes(n)
# print(res)
# #
# n = [0, 0, 1]
# res = moveZeroes(n)
# print(res)
