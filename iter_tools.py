# Enter your code here. Read input from STDIN. Print output to STDOUT
from itertools import permutations
a=int(input())
b=list(input().split(' '))
c=int(input())
f=(list(permutations(b, c)))
o=len(f)
count=0

for i in f:
    print(i)
    for k in i:
        if k=='a':
            count+=1
            break
ans=count/o
print(round(ans,4))