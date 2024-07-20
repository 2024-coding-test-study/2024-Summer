#https://codeup.kr/problem.php?id=6097  <=== 요기 URL 로 가면 코드업 기초 100제 마지막에서 2번째 문제인 설탕과자 설탕과자 뽑기문제이다.

h,w=map(int,input().split())
n=int(input())
info=[]
for _ in range(n):
    r=list(map(int,input().split()))
    info.append(r)


squ=[[0]*w for i in range(h)]

for i in info:
    x=i[2]
    y=i[3]
    x=x-1
    y=y-1
    
    if i[1]==0:
        for c in range(i[0]):
            squ[x][y+c]=1
    elif i[1]==1:
        for d in range(i[0]):
            squ[x+d][y]=1

print()

def print_result(lst):
    for a in lst:
        for b in a:
            print(b,end=' ')
        print()

print_result(squ)
