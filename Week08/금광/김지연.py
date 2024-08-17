t = int(input())

def init_mine(mine, x, data_lst):
  mine[x] = data_lst

for _ in range(t):
  n, m = map(int, input().split())
  mine = [[0] for _ in range(n)]

  data = list(map(int, input().split()))
  for i in range(n):
    init_mine(mine, i, data[i*m:i*m+m])
  
  #완전탐색 시작
  #문제에서 첫번째 어느 행에서든 시작해도 상관없다고 했지만 0번재 행부터 시작해야 금의 최댓값을 구할 수 있음.
  for col in range(1, m):
    #각 행 값을 최대값으로 변경해주기
    for row in range(n):
      if row == 0:#0번째 행에 위치한 요소는 left_up이 없음
        left_up = 0
      else:
        left_up = mine[row-1][col-1]
      if row == n-1: #맨 마지막 행에 위치한 요소는 left_down이 없음
        left_down = 0
      else:
        left_down = mine[row+1][col-1]
      left = mine[row][col-1]

      mine[row][col] = max(left_up, left_down, left) + mine[row][col]
 

  answer = 0
  for i in range(n):
    answer = max(answer, mine[i][m-1])
  print(answer)
