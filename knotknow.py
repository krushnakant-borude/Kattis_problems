n=int(input())
a=input().split()
b=input().split()
ls2=[]
ls1=[]

for i in range(n):
    ls1.append(int(a[i]))
    
for j in range(n-1):
    ls2.append(int(b[j]))

print(sum(ls1)-sum(ls2))

