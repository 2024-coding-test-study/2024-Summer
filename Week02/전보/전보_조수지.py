import heapq
import sys
input = sys.stdin.readline
INF = int(1e9)

n, m, c = map(int, input().split())

# 도시 초기화
city = [[] for i in range(n + 1)]
# 거리 리스트 무한으로 초기화
distance = [INF] * (n + 1)

# 입력받은 값을 도시 리스트에 저장
for _ in range(m) :
  x, y, z = map(int, input().split())
  city[x].append((y, z))
  
# 다익스트라 함수 만들기
def dij(c) :
  q = []
  
  # 시작 노드의 최단 경로는 0
  heapq.heappush(q, (0, c))
  distance[c] = 0
  
  # 큐가 빌 때까지 반복
  while q :
    dist, now = heapq.heappop(q) # 우선순위 큐에 따라 하나를 pop
    
    if distance[now] < dist : # pop한 값보다 작은 값이면 무시
      continue
    
    for i in city[c] :
      cost = dist + i[1]
      
      if cost < distance[i[0]] : # 현재 노드에서 다른 노드로 이동 거리가 짧으면
        distance[i[0]] = cost 
        heapq.heappush(q, (cost, i[0])) # 우선순위 큐에 집어넣어줌
   
# 시작 지점에서 다익스트라 수행     
dij(c)

cnt = 0
max_dis = 0

# 거리 리스트에서 무한이 아니면 cnt를 늘려줌
for i in distance :
  if i != INF :
    cnt += 1
    max_dis = max(max_dis, i) # 가장 먼 도시의 최단거리를 구해줌
    
print(cnt - 1, max_dis)