from collections import deque

n, m = map(int, input().split())
maze = []

for i in range(n) :
  maze.append(list(map(int, input())))
  
# x, y좌표를 상하좌우로 움직일 수 있는 리스트 만들어주기
move_x = [-1, 1, 0, 0]
move_y = (0, 0, -1, 1)

def bfs(x, y) :
  queue = deque() # bfs이기 때문에 deque()로 큐를 만들어 줌
  queue.append((x, y)) # list에 x, y좌표를 넣음 
  
  while queue : # list에 있는게 없을 때까지 반복해줌
    x, y = queue.popleft() # list에서 pop 한 값 저장
    
    for i in range(4): # 상하좌우에 0이 있는지 확인
      nx = x + move_x[i]
      ny = y + move_y[i]
      
      if nx < 0 or nx >= n or ny < 0 or ny >= m : # 범위를 벗어나면 무시
        continue
      
      if maze[nx][ny] == 0 : # 0을 만나면 이동 불가능하니까 무시
        continue
      
      if maze[nx][ny] == 1 : # 1을 만나면 이동 가능하기에 큐에 추가
        maze[nx][ny] = maze[x][y] + 1 
        queue.append((nx, ny))
        
  return maze[n-1][m-1] # 탈출구 좌표의 값을 반환

print(bfs(0, 0))