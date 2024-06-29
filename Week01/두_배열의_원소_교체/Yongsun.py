N=int(input())
plans=input().split()
a=1
b=1

def way(n):
    global a,b
    if n=='R':
        c=b+1
        if c<1 or c>N:
            pass
        else:
            b=c    
    elif n=='L':
        c=b-1
        if c<1 or c>N:
            pass
        else:
            b=c
    elif n=='U':
        c=a-1
        if c<1 or c>N:
            pass
        else:
            a=c
    elif n=='D':
        c=a+1
        if c<1 or c>N:
            pass
        else:
            a=c
for i in plans:
    way(i)

print(a,b)
