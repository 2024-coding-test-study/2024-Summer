#1번에서 k
#k번에서 x
#각각 최소거리 구하기(다익스트라) -> 플로이드 워셜 알고리즘으로 변경 최악의 경우 100^3밖에 안됨
import sys
import heapq
input = sys.stdin.readline
INF = int(1e10)

n, m = map(int, input().split())
graph = [[INF] * (n+1) for _ in range(n+1)]
distance = [INF] * (n+1)

#자기자신은 0으로 초기화 -> 대각선
for i in range(n+1):
  graph[i][i] = 0
  
#간선 정보 입력
for i in range(m):
  a, b = map(int, input().split())
  graph[a][b], graph[b][a] = 1, 1
  
x, k = map(int, input().split())

for k in range(1, n+1):
  for a in range(1, n+1):
    for b in range(1, n+1):
      graph[a][b] = min(graph[a][b], graph[a][k] + graph[k][b])

#1->k->x
result = graph[1][k] + graph[k][x]
if result >= INF:
  print(-1)
else print(result)