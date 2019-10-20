a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]

b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]

r = []
for x in a:
    if x in b:
        r.append(x)

c = [1,1,1,1,7,6,9,12]
d = [1,1,1,1,2,3,4,5,6,7]
i = []
for u in c:
    if u in d:
        i.append(u)
        
print(i)
