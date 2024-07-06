#dfs는 스택 -> 재귀함수
#dfs로 x,y넘길때 기존 x, y좌표에 dx와 dy를 더하지 않음
#처음에 bfs로 풀까하다가 0을 중심으로 깊게 파고드는게 더 간단할 거 같았음
#풀이시간: 42m 22s

n, m = map(int, input().split())
data = list(list(map(int, input())) for _ in range(n))

#상하좌우
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


cnt = 0
def dfs(graph, x, y):
  if x >= n or x < 0 or y >= m or y < 0:
    return 
  if graph[x][y] != 1:
    graph[x][y] = 1 #방문처리
    #x,y에서 상하좌우 탐색
    for i in range(4):
      dfs(graph, x + dx[i], y + dy[i])
    return True #아이스크림이 있는 칸
  else: #해당 좌표가 칸막이이거나 이미 방문을 했다면
    return False

#최대 1000 * 1000
for x in range(n):
  for y in range(m):
    if dfs(data, x, y):
      cnt += 1
    
print(cnt)
