from collections import Counter

def topKFrequentElement(nums, k):
    """
    Return Top k frequent elements of a list. Below method is the one using built-in Counter, lambda function, etc. 
    TODO: Bruteforce, and other methods such as bucket sort. 
    """
    result = []
    counter = Counter(nums)  # returns a dictionary of items and their counts. Order is according to the items in the list 

    # Custom sorting using lambda function. x[1] is because individual item and its count are stored as a tuple inside the counter.
    # to prioritize the second element of the tuple, which is the count of the item, x[1] is used. Reverse is True to sort in a descending order. 
    sortedCounter = dict(
        sorted(counter.items(), key=lambda x: x[1], reverse=True))  
    for key in sortedCounter.keys():
        result.append(key)  # create a list with the most frequent counts
    return result[:k]  # return only k counts. 


nums2 = [1, 1, 2, 2, 1, 2, 2]
nums3 = [-2, -3, -2, 5, -2, 5, -2, 5, -3, -2]
print(f"for nums2: {topKFrequentElement(nums2, 2)}")
print(f" for nums3: {topKFrequentElement(nums3, 2)}")
