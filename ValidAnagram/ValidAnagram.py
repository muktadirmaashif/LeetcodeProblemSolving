def ValidAnagram(s, t):
    # """
    # Brute force, using list.
    # Since string is immutable converting strings to lists.
    #
    # """
    # list_s = []
    # list_t = []
    # if len(s) != len(t):
    #     return False
    # else:
    #     for i in s:
    #         list_s.append(i)
    #     for i in t:
    #         list_t.append(i)        
    #     for i in range(len(list_s)):
    #         if list_s[i] in list_t:
    #             list_t.remove(list_s[i]) # If the character matches, is removed from the maching list
    #     if list_t != []: # checking if the matching list is empty
    #         return False
    #     else:
    #         return True
    #
    # """
    # Using a dictionary to keep track of the characters frequency
    # """
    # dict = {}
    # result = True 
    # count = 0
    # if len(s) != len(t):
    #     result = False
    # for i in s:
    #     if i in dict.keys():
    #         dict[i] +=1
    #     else:
    #         dict[i] = 1
    # for i in t:
    #     if i in dict.keys():
    #         dict[i] -= 1  # decreases frequency by 1 if matches 
    # for val in dict.values(): 
    #     if val != 0:  # by now, all values should be zero if all characters frequency are the same
    #         result = False
    # return result

    res = True 
    for i in t:
        countS = s.count(i)
        countT = t.count(i)
        # print(countS, countT)
        if countS != countT:
            res = False 
            break
    if len(s) != len(t):
        return False
    elif res:
        return True
    else:
        return False

s1="anagram"
t1= "nagaram"
print(ValidAnagram(s1, t1))

s2="rat"
t2="art"
print(ValidAnagram(s2, t2))

s3="rat"
t3="car"
print(ValidAnagram(s3, t3))

s4="aacc"
t4="ccac"
print(ValidAnagram(s4, t4))

s4="a"
t4="ac"
print(ValidAnagram(s4, t4))
