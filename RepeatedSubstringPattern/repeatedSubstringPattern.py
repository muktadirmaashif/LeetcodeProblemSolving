# def repeatedSubstringPattern(s: str) -> bool:
    # lenS = int(len(s)/2)
    # iterator = range(lenS)
    # for i in iterator:
    #     subS = s[:i+1]
    #     subCount = s.count(subS)
    #     # return True if s.count(subS) > 1 else False
    #     print(subCount)
    #     if subS * subCount == s:
    #         return True
    # return False

# found this solution in leetcode
# If a string is concatanated with itself, remove the first and last character of the concatanated string, and the original string is found in the sliced version of concatanated string, then the original string is made of repeated stubstring. 
def repeatedSubstringPattern(s: str):
    concS = s + s 
    sliceS = concS[1:-1]
    if s in sliceS:
        print(sliceS)
        return True
    return False
    # one liner
   # return s in (s+s)[1:-1]
    
    
s = "abab"
res = repeatedSubstringPattern(s)
print(res)

s = "aba"
res = repeatedSubstringPattern(s)
print(res)

s = "aaaa"
res = repeatedSubstringPattern(s)
print(res)

s = "abcabcabc"
res = repeatedSubstringPattern(s)
print(res)
