def flip(n):
    a=0
    for i in range(len(n)-1):
        if n[i]!=n[i+1]:
            a+=1
    a=a+1
    answer=a//2
    return answer

n='01011010001001'
print(flip(n))
