n=int(input())
a=input().split()
ls=[]

for x in a:
    ls.append(int(x))


x=ls.index(min(ls))   
print(x)