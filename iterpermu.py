from itertools import permutations
s=list(input().split(' '))
p=list(permutations(s[0],int(s[1])))
l=[]
for i in p:
    k=''.join(i)
    l.append(k)
l.sort()
for g in l:
    print(g)