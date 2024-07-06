from collections import deque

#풀이시간: 28m 40s
# 소스코드 날라가서 두번 풂..
#이전 노드를 중심으로 상하좌우 bfs탐색 -> 이전 노드에는 해당 노드를 방문하기 위한 최소 노드 개수가 적혀져 있으므로 상하좌우 탐색하면서 이전 노드에 적힌 수 + 1을 하면 다음 노드로 가기 위한 최소 노드 개수를 구할 수 있음
n, m = map(int, input().split())
map = list(list(map(int, input())) for _ in range(n))
#노드를 한번만 방문해서 마지막칸에 도착하는게 최소 노드개수
dx = [-1, 1, 0 ,0]
dy = [0, 0, -1 ,1]
def bfs():
  q = deque()
  q.append((0,0))
  while q:
    x, y = q.popleft()
    #상하좌우 bfs
    for i in range(4):
      nx = x + dx[i]
      ny = y + dy[i]
      if nx < 0 or nx >= n or ny < 0 or ny >= m:
        continue
      if map[nx][ny] == 0:
        continue
      if map[nx][ny] == 1:
        #방문처리
        map[nx][ny] = map[x][y] + 1
        q.append((nx, ny))
  return print(map[n-1][m-1])
        
bfs()