from rich import print
from rich.traceback import install
install()


def mejorityElement(nums):
    # Solution 1
    # Using dictionary. T.C. O(n), S.C. O(n)
    n = len(nums)
    freq = {}  # frequency number of each element of nums as {num: frequency}

    for i in nums:
        if i not in freq:
            freq[i] = 1
        else:
            freq[i] += 1
    for key, val in freq.items():  # check which frequency meets the condition
        if val >= n/2:
            return (key)

    # Solution 2
    # Using sort, T.C. O(n), S.C. O(nlongn)
    nums.sort()
    current = nums[0]
    freq = 1
    result = 0
    if len(nums) == 1:  # takes care of [1] type list
        return nums[0]
    else:
        for next in nums[1:]:  # iterate from 1th element
            if current == next:
                freq += 1
                if freq >= len(nums)/2:  # check freequency condition
                    result = current
            else:
                current = next
                freq = 1
        return result


nums1 = [3, 4, 3]
nums2 = [2, 2, 1, 1, 1, 2, 2]
nums3 = [-2, -3, -2, 5, -2, 5, -2, 8, 1, -2]
nums4 = [1]

print(f"{nums1}, {mejorityElement(nums1)}")
print(f"{nums2}, {mejorityElement(nums2)}")
print(f"{nums3}, {mejorityElement(nums3)}")
print(f"{nums4}, {mejorityElement(nums4)}")
