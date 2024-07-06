from collections import deque
#음료수 얼려먹기는 교재에 DFS로 풀게 되어 있는데 BFS로 풀어봤습니다.
#보시다시피 쉽진 않습니다. 그래도 BFS가 속도가 좀더 빠르니까 이렇게 풀었어요.
n,m=map(int,input().split())

graph=[]
for i in range(n):
    graph.append(list(map(int,input())))

dx=[-1,1,0,0]
dy=[0,0,-1,1]
result=0

# for x와 y 돌리는건 그냥 좌표 하나씩 세는거입니다.
for x in range(n):
    for y in range(m):
        if graph[x][y]==0:
            queue=deque()
            queue.append((x,y))
            graph[x][y]=1
            #여기서 가장 중요한것은 위에 좌표 세는 x,y와 아래 큐에 담는 좌표의 변수를 a,b로 따로 구분해줘야 합니다. 아래와 밑에 둘다 밑에 x,y 로 변수 통일하면 계산이 꼬입니다.
            #밑부터는 BFS로 큐가 빌때까지 한번에 다 탐색하는 것이고 그리고 result 값에 1씩 더해서 세주는것입니다.
            while queue:
                a,b=queue.popleft()
                
                for i in range(4):
                    c=a+dx[i]
                    d=b+dy[i]
                    if c<0 or d<0 or c>=n or d>=m:
                        continue
                    if graph[c][d]==1:
                        continue
                    if graph[c][d]==0:
                        graph[c][d]=1
                        queue.append((c,d))
            result+=1
print(result)
