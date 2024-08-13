def firstOccuranceInAString(h, n):
    hL = len(h)
    nL = len(n)

    # for i in range(hL - nL +1):
    #     match = True
    #     for j in range(nL):
    #         print(f"i+j = {i+j}, j = {j}")
    #         if h[i+j] != n[j]:
    #             match = False
    #             break
    #     if match:
    #         print("i = ", i)
    #         return i
    # return -1

    res = []
    for id in range(hL-nL+1):
        sliced = h[id:nL+id]
        if sliced == n:
            res.append(id)
            return id 

    return -1  
            
        # sliced = h[0:3] = "sad"
        # if sliced == n
        #   result = h[0]
        # sliced = h[1:4]
        #   if sliced == n

h="sadbutsad"
n="sad"
print(f"{h}, {n}, {firstOccuranceInAString(h, n)}")

h="sadbutsalt"
n="sad"
print(f"{h}, {n}, {firstOccuranceInAString(h, n)}")

h="butsadbut"
n="sad"
print(f"{h}, {n}, {firstOccuranceInAString(h, n)}")

h="nothingbuthappy"
n="sad"
print(f"{h}, {n}, {firstOccuranceInAString(h, n)}")

h="saltychill"
n="sad"
print(f"{h}, {n}, {firstOccuranceInAString(h, n)}")
