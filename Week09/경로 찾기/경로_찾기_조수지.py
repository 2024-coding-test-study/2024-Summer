n = int(input()) # 정점의 개수
graph = []

# 입력 받은 값을 리스트에 넣기
for i in range(n) :
  graph.append(list(map(int, input().split())))
  
# 플로이드-워셜 알고리즘을 통해 경로 찾기
for k in range(n):
  for i in range(n):
    for j in range(n): # i에서 k를 거쳐 j로 가는 경로가 있다면
      if graph[i][k] and graph[k][j] : # ★ 이 조건이 없으면 방향 그래프X
        graph[i][j] = 1
            
# 경로 출력
for i in range(n) :
  for j in range(n) :
    print(graph[i][j], end=' ')
  print()