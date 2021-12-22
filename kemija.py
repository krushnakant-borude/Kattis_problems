lvowel=["a","e","i","o","u"]
n=input().split()

def remove(word):
    ls=list(word)
    for x in lvowel:
        for x in ls:
            ls.pop((int(ls.index(x))+1))
            ls.pop((int(ls.index(x))+2))
        
    str=""
    for i in range(len(ls)):
        str+=ls(i)
    return str
    
    


for x in n:
    bb=remove(x)
    print(bb)


