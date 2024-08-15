def plusOne(digits: list[int]) -> list[int]:
    pass

s ="" 
l = [9, 9, 9, 9]
l =[9,8,7,6,5,4,3,2,1,0] 
# l = [9]
for i in l:
    s += str(i)
print(s)
sL = []
sL = list(str(int(s)+1)) 
print(sL)
for i in range(len(sL)):
    sL[i] = int(sL[i])

print(sL)

