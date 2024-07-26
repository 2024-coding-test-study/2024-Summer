import sys
input = sys.stdin.readline # 이걸 안하면 시간 초과 뜸

n, m = map(int, input().split()) # 세로, 가로 입력받기
MAP = [list(map(int, input().split())) for _ in range(n)] # 지도 정보 입력받아 초기화
WALL_MAP = [[0] * m for _ in range(n)] # 벽 설치된 지도
# 네 방향 설정
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]
result = 0

# 바이러스 확산 함수
def virus(x, y) :
  for i in range(4) : # 네 방향에 대해 모두 확인
    nx = x + dx[i]
    ny = y + dy[i]
    
    # 바이러스가 퍼질 수 있다면
    if nx >= 0 and nx < n and ny >= 0 and ny < m and WALL_MAP[nx][ny] == 0 :
        WALL_MAP[nx][ny] = 2 # 확산 시킨 다음
        virus(nx, ny) # 확산된 위치에서 다시 확산 되는지 확인
        
# 안전 영역 계산 함수
def get_score() :
  score = 0
  
  for i in range(n) : 
    for j in range(m) : # 지도 전체에 대하여
      if WALL_MAP[i][j] == 0 : # 빈칸의 개수 세기
        score += 1
  
  return score

def dfs(count) :
  global result
  
  if count == 3 : # 벽을 3개 세운 다음 확산 시작
    for i in range(n) :
      for j in range(m) :
        WALL_MAP[i][j] = MAP[i][j]
     
    for i in range(n) : # 바이러스 확산
      for j in range(m) :
        if WALL_MAP[i][j] == 2 :
          virus(i, j)
    
    # 안전 구역 계산
    result = max(result, get_score())
    return result
    
  for i in range(n) :
    for j in range(m) : # 지도 전체에 대하여
      if MAP[i][j] == 0 : # 빈칸이라면
        MAP[i][j] = 1 # 일단 벽을 설치
        count += 1 # 벽 개수 1 더하기
        
        dfs(count) # 다음 벽 설치하기 위해 dfs 실행
        
        MAP[i][j] = 0 # 원상복구
        count -= 1 # 벽 개수 1 빼기
        
dfs(0)

print(result)