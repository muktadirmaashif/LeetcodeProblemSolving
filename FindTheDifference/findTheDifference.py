def findTheDifference(s: str, t: str) -> str:
    res = ""
    t_dict = {}
    for i in t:
        if i in t_dict:
            t_dict[i] += 1 
        else:
            t_dict[i] = 1
    for i in s:
        if i in t_dict:
            t_dict[i] -= 1
        print(t_dict)
    for key, val in t_dict.items():
        if val == 1:
           return key 

s = "abc"
t = "abcd"
print(findTheDifference(s, t))

s = "a"
t = "aa"
print(findTheDifference(s, t))

s = "ae"
t = "aea"
print(findTheDifference(s, t))
