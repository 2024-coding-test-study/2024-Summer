n=int(input())
direction=input().split()
dx=[-1,1,0,0]
dy=[0,0,-1,1]
a={'L':0,'R':1,'U':2,'D':3}
x,y=1,1
for i in direction:
   c,d=x+dx[a[i]],y+dy[a[i]]
   if 1>c or c>n or 1>d or d>n:
      continue
   x,y=c,d
print(x,y)
