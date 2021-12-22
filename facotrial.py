def factorial(lol):
    if lol==1 or lol==0:
        return 1
    return lol*factorial(lol-1)


n=int(input())
for i in range(n):
    a=int(input())
    factls=list(str(factorial(a)))
    factls.reverse()
    print(int(factls[0]))
