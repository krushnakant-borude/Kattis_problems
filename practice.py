n=(input())

a=len(n)

whitespace=n.count("_")

def uppercase(wo):
    count=0
    for d in wo:
        if d.isupper():
            count+=1
    return count
    

def lowercase(wo):
    count=0
    for d in wo:
        if d.islower():
            count+=1
    return count

symbol=a-(int(uppercase(n))+int(lowercase(n)+whitespace))

print(whitespace/a)
print(int(lowercase(n))/a)
print(int(uppercase(n))/a)
print(symbol/a)