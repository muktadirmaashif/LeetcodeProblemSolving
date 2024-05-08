


def containsDuplicate(nums):
# Brute force. T.C. O(n^2)
    l = len(nums)
    result = False
    for i in range(l):
        for j in range(i+1, l):
            # print(f"i: {i}, j: {j}")
            # print(f"nums[{i}]: {nums[i]}, nums[{j}]: {nums[j]}")
            if nums[i] == nums[j]:
                # print("True")
                result = True
    return result

# with sorting. T.C. O(nlongn)
    nums.sort()
    l = len(nums)
    res = False
    current = nums[0]
    frequency = 1
    for next in nums[1:]:
        if next == current:
            res = True
        else:
            current = next
    return res

# with Dictionary. T.C. O(n), S.C. O(n)
    dict = {} 
    l = len(nums)
    result = False
    for i in nums:
        if i not in dict:
            dict[i] = 1 
        else:
            dict[i] += 1 
            if dict[i] > 1:
                result = True
    return result

list1 = [1, 2, 3, 1]
list2 = [1, 2, 2, 3]
list3 = [3]
list4 = [2, 14, 18, 22, 22] 

print(f"list1: {containsDuplicate(list1)}")
print(f"list2: {containsDuplicate(list2)}")
print(f"list3: {containsDuplicate(list3)}")
print(f"list4: {containsDuplicate(list4)}")
