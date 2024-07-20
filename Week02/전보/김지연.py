import heapq
import sys
input = sys.stdin.readline
INF = int(1e10)

n, m, c = map(int, input().split())
graph = [[] for _ in range(n+1)]
distance = [INF] * (n+1)
#간선정보 입력
for i in range(m):
  a, b, c = map(int, input().split())
  graph[a].append((b,c)) #a노드에 b가 연결되어있고 거리는 c이다.

def dijkstra(start):
  q = []
  heapq.heappush(q, (0, start))
  distance[start] = 0
  while q:
    dist, now = heapq.heappop(q)
    if dist > distance[now]:
      continue
    #now에 연결된 노드
    for i in graph[now]:
      cost = dist + i[1]
      if cost < distance[i[0]]:
        distance[i[1]] = cost
        heapq.heappush((cost, i[0]))

#다익스트라 실행
dijkstra(c)
#c에서 갈 수 있는 노드 수 세기 -> distance가 INF보다 작은거 세기
count = 0
max_dist = 0 #distance에서 최대 정수 저장하면 그게 총 걸리는 시간
for d in distance:
  if d < INF:
    count += 1
    max_dist = max(max_dist, d)
print(count-1, max_dist) #시작 노드는 count에 포함되면 안됨
  