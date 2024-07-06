n , m = map(int, input().split()) # 세로, 가로 숫자 입력받기
case = [] # 얼음틀

for i in range (n) : # 얼음틀 초기화 시켜주기. 
  case.append(list(map(int, input())))
  
# 0으로만 이어진 곳이 몇개인지 찾는 것이 관건.


def dfs(x, y) :
  if x < 0 or x > n - 1 or y < 0 or y > m - 1 : # 좌표가 얼음틀의 범위를 벗어나면
    return False
  
  if case[x][y] == 0 : # 0을 찾았으면
    case[x][y] = 7 # 지나갔다는 뜻으로 임의로 값을 7로 바꿔줌
    
    # 상하좌우 좌표에 대해서도 0인지 확인해준다
    dfs(x - 1, y) # 상
    dfs(x + 1, y) # 하
    dfs(x, y - 1) # 좌
    dfs(x, y + 1) # 우
    return True
  
  return False

cnt = 0

# 얼음틀 하나하나를 탐색하며 0으로 이어진 공간의 개수 찾기
for i in range(n) :
  for j in range(m) :
    if dfs(i, j) == True :
      cnt += 1
      
print(cnt)