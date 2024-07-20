INF = int(1e9) # 무한 설정

n, m = map(int, input().split())

# 회사 경로 그래프 무한으로 초기화
company = [[INF] * (n + 1) for _ in range(n + 1)]

# 서로 연결된 회사 입력 받기
for i in range (m) :
  com1, com2 = map(int, input().split())
  company[com1][com2] = 1
  company[com2][com1] = 1
  
x, k = map(int, input().split())

# 플로이드 워셜 알고리즘
for i in range(1, n + 1) :
  for j in range(1, n + 1) :
    for k in range(1, n + 1) :
      company[j][k] = min(company[j][k], company[j][i] + company[i][k])
  
# 1에서 시작하므로 1에서 k까지의 거리와 k에서 x까지 거리를 더해줌    
distance = company[1][k] + company[k][x]

# 만약 갈 수 없는 경로라면 -1 출력
if distance >= INF :
  print("-1")
else :
  print(distance)